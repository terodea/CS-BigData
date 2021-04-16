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