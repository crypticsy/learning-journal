<h3>Understanding Datasets</h3>
<table style="width:100%;">
    <tr>
        <th>Function</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>dataframe.head(n)</td>
        <td>to show the first n rows of dataframe || else top 5</td>
    </tr>
    <tr>
        <td>dataframe.tail(n)</td>
        <td>to show the bottom n rows of dataframe  || else bottom 5</td>
    </tr>
    <tr>
        <td>dataframe.shape</td>
        <td>size of dataframe (rows, columns)</td>
    </tr>
    <tr>
        <td>dataframe.dtypes()</td>
        <td>to check data types</td>
    </tr>
    <tr>
        <td>dataframe.describe()</td>
        <td>returns a statistical summary</td>
    </tr>
    <tr>
        <td>dataframe.describe(include="all")</td>
        <td>returns a statistical summary of all including objects</td>
    </tr>
    <tr>
        <td>dataframe.info()</td>
        <td>provides a concise summary of all your dataframe</td>
    </tr>
    <tr>
        <td>dataframe.astype()</td>
        <td>to convert data types</td>
    </tr>
    <tr>
        <td>dataframe.columns.values</td>
        <td>to get a array of column headers from </td>
    </tr>
    <tr>
        <td>dataframe.index.values</td>
        <td>to get a array of index</td>
    </tr>
</table>

<br/>

<h3>Dataframe Manipulation</h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>dataframe.set_index("key", inplace=True)</td>
        <td>changes the index of the dataframe to given column "key"</td>
    </tr>
    <tr>
        <td>dataframe.reset_index()</td>
        <td>resets the index of the dataframe</td>
    </tr>
    <tr>
        <td>dataframe.dropna(axis=0)</td>
        <td>drops the entire row if found empty</td>
    </tr>
    <tr>
        <td>dataframe.dropna(axis=1)</td>
        <td>drops the entier column if found empty</td>
    </tr>
    <tr>
        <td>dataframe.dropna( [keys] ,inplace=True)</td>
        <td>applies changes to the actual dataframe itself</td>
    </tr>
    <tr>
        <td>dataframe.replace( missing_value, new_value )</td>
        <td>replace value of one to another in dataframe</td>
    </tr>
    <tr>
        <td>dataframe.rename( columns={prevkey:newkey} )</td>
        <td>rename columns of the dataframe</td>
    </tr>
    <tr>
        <td>dataframe.sum(  axis=1  )</td>
        <td>returnsm sum of the row</td>
    </tr>
    <tr>
        <td>dataframe["key"].std()</td>
        <td>returns the standard deviation</td>
    </tr>
    <tr>
        <td>dataframe["key"].mean()</td>
        <td>returns the mean of the column</td>
    </tr>
    <tr>
        <td>pd.get_dummies(df[column])</td>
        <td>Convert categorical variables to dummy variables (0 or 1) [One - hot encoding]</td>
    </tr>
    <tr>
        <td>dataframe.groupby([column, column])</td>
        <td>Group dataframe based on column</td>
    </tr>
    <tr>
        <td>dataframe[column].agg('function')</td>
        <td>Perform an operation in a particular coulmn</td>
    </tr>
</table>

<br/>

<h3>Viewing Datasets </h3>
<table style="width:100%;">
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>dataframe.loc[label]</td>
        <td>filters by the labels of the index/column
        <br/><br/># For val of particular col and row use dataframe.loc['label','col']</td>
    </tr>
    <tr>
        <td>dataframe.iloc[index]</td>
        <td>filters by the position of the index/coumn</td>
    </tr>
</table>

<br/>

<h3>Miscellaneous</h3>
<table style="width:100%;">
    <tr>
        <th>Data Format</th>
        <th>Read</th>
        <th>Save</th>
    </tr>
    <tr>
        <td>csv</td>
        <td>pd.read_csv()</td>
        <td>df.to_csv()</td>
    </tr>
    <tr>
        <td>json</td>
        <td>pd.read_json()</td>
        <td>df.to_json()</td>
    </tr>
    <tr>
        <td>Excel</td>
        <td>pd.read_excel()</td>
        <td>df.to_excel()</td>
    </tr>
    <tr>
        <td>sql</td>
        <td>pd.read_sql()</td>
        <td>df.to_sql()</td>
    </tr>
</table>
