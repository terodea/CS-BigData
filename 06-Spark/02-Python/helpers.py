import pandas as pd
from collections import Iterable
from collections import OrderedDict
from pyspark.resultiterable import ResultIterable
from pyspark import sql


def rename_columns(df, columns):
    """
    sparkDf = rename_columns({'a':'a1', 'b':'b1'})
    """
    try:
        if isinstance(columns, dict):
            for old_name, new_name in columns.items():
                df = df.withColumnRenamed(old_name, new_name)
            return df
        else:
            raise ValueError("'columns' should be a dict, like {'old_name_1':'new_name_1', 'old_name_2':'new_name_2'}")
    except Exception as e:
        raise e

def _flatten(l):
    """Return one RDD or multiple joined RDDs in a flattened list."""
    if isinstance(l, ResultIterable):
        yield list(l)
    else:
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, ResultIterable):
                for sub in _flatten(el):
                    yield sub
            else:
                yield el


def _to_pandas(x):
    """Convert a RDD to a pandas DataFrame."""
    return pd.DataFrame((row.asDict() for row in x))

def _to_rows(df, by, k):
    """Convert to a list of Row objects."""
    if isinstance(by, str):
        by, k = [by], [k]
    if isinstance(df, pd.Series):
        df = df.to_frame().T
    if isinstance(df, pd.DataFrame):
        for col, val in zip(by, k):
            df[col] = val
        df.columns = map(str, df.columns)  # Else Row() will fail
        rows = (sql.Row(**OrderedDict(sorted(x.items())))
                for x in df.to_dict(orient='records'))
    else:
        # It's hopefully only a value.
        result = ((k, v) for k, v in zip(by + ['value'], k + [df]))
        rows = (sql.Row(**OrderedDict(sorted(result))),)
    return rows

def udaf(by, func, *args, **kwargs):
    """Apply a user defined aggregate function on PySpark DataFrame(s).
    PySpark DataFrames (or RDDs with Row objects) in args are passed to func()
    as pandas DataFrames in the same order.
    func() should return a pandas DataFrame, pandas Series (all values for a
    single row/observation) or a single value (returned in a column 'value').
    :param by: Column or list of columns to group by
    :param func: Function to apply to each group
    :param args: PySpark DataFrames
    :param kwargs: Keyword arguments (optional):
        * n_partitions: Number of partitions to use for the rdd.groupby
        * schema: Schema for PySpark DataFrame
        * other kwargs are passed to func
    :return PySpark DataFrame with aggregates
    Note:
    * If a group by key is missing in one of the DataFrames, it's not passed to
        the aggregate function (an inner join is used).
    """
    n_partitions = kwargs.pop('n_partitions', 200)  # Python 3 would solve this
    schema = kwargs.pop('schema', None)
    grouped = _group_data(by, *args, n_partitions=n_partitions)
    result = (
        grouped
        .flatMap(lambda x: _to_rows(func(*map(_to_pandas, _flatten(x[1])),
                                         **kwargs),
                                    by, x[0]))
    )
    return result.toDF(schema)


def _group_data(by, *args, **kwargs):
    """Group DataFrame as RDD by key and join grouped RDDs by key."""
    n_partitions = kwargs.pop('n_partitions', 200)
    grouped = _group(args[0], by, n_partitions)
    for other in args[1:]:
        grouped = grouped.join(_group(other, by, n_partitions))
    return grouped


def _group(data, by, n_partitions=None):
    """Group by using RDD method."""
    if isinstance(data, sql.DataFrame):
        rdd = data.rdd
    else:
        rdd = data
    if n_partitions:
        rdd = rdd.repartition(n_partitions)
    if isinstance(by, list):
        return rdd.groupBy(lambda x: tuple(x[b] for b in by))
    else:
        return rdd.groupBy(lambda x: x[by])

def column_to_list(df, col_name):
    return [x[col_name] for x in df.select(col_name).collect()]


def two_columns_to_dictionary(df, key_col_name, value_col_name):
    k, v = key_col_name, value_col_name
    return {x[k]: x[v] for x in df.select(k, v).collect()}
