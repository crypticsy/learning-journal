## Keyboard Shortcuts

| Shortcut        | Description                |
| --------------- | -------------------------- |
| Tab             | Go to next cell in the row |
| cmd + shift + v | Paste values without style |
| cmd + d         | Fill down                  |
| cmd + a         | Select entire sheet        |

---

### Functions

#### Numbers

| Function | Description |
|----------|-------------|
| `=MAX(A1:A10)` | Returns the maximum value in the range |
| `=MIN(A1:A10)` | Returns the minimum value in the range |
| `=SUM(A1:A10)` | Returns the sum of the values in the range |
| `=AVERAGE(A1:A10)` | Returns the average of the values in the range |
| `=COUNT(A1:A10)` | Returns the number of values in the range |
| `=COUNTA(A1:A10)` | Returns the number of non-empty values in the range |
| `=COUNTBLANK(A1:A10)` | Returns the number of empty values in the range |
| `=COUNTIF(A1:A10, ">10")` | Returns the number of values in the range that are greater than 10 |
| `=COUNTIFS(A1:A10, ">10", B1:B10, "<20")` | Returns the number of values in the range that are greater than 10 and less than 20 |
| `=SUMIF(A1:A10, ">10")` | Returns the sum of the values in the range that are greater than 10 |
| `=SUMIFS(A1:A10, ">10", B1:B10, "<20")` | Returns the sum of the values in the range that are greater than 10 and less than 20 |
| `=AVERAGEIF(A1:A10, ">10")` | Returns the average of the values in the range that are greater than 10 |
| `=AVERAGEIFS(A1:A10, ">10", B1:B10, "<20")` | Returns the average of the values in the range that are greater than 10 and less than 20 |
| `=IF(A1>10, "Greater than 10", "Less than 10")` | Returns "Greater than 10" if the value in A1 is greater than 10, otherwise returns "Less than 10" |
| `=OR(A1>10, B1>10)` | Returns TRUE if either A1 or B1 is greater than 10 |
| `=SUMIF(A1:A10, ">10", B1:B10)` | Returns the sum of the values in the range B1:B10 if the value in the range A1:A10 is greater than 10 |

> **Note:** You can also return a formula in an IF statement (e.g. `=IF(A1>10, A1*2, A1*3)`)

#### Dates

| Function | Description |
|----------|-------------|
| `=YEAR(TODAY())` | Returns the current year |
| `=TEXT(YEAR(TODAY()),"YY")` | Returns the current year in two-digit format |
| `=TEXT(TODAY(),"DD/MM/YYYY")` | Returns the current date in DD/MM/YYYY format |
| `=MONTH(TODAY())` | Returns the current month |
| `=DAY(TODAY())` | Returns the current day |
| `=WEEKDAY(TODAY())` | Returns the current day of the week (e.g. 1 for Sunday, 2 for Monday, etc.) |
| `=TEXT(TODAY(),"dddd")` | Returns the current day of the week (e.g. Sunday, Monday, etc.) |
| `=DATE(YEAR(TODAY()), MONTH(TODAY()), DAY(TODAY())+1)` | Returns the date of tomorrow |

#### Text

| Function | Description |
|----------|-------------|
| `=CONCATENATE(A1, " ", B1)` | Returns the concatenation of the values in A1 and B1 |
| `=LEFT(A1, 5)` | Returns the first 5 characters of the value in A1 |
| `=RIGHT(A1, 5)` | Returns the last 5 characters of the value in A1 |
| `=MID(A1, 5, 10)` | Returns 10 characters of the value in A1 starting from the 5th character |
| `=LEN(A1)` | Returns the length of the value in A1 |
| `=LOWER(A1)` | Returns the value in A1 in lower case |
| `=UPPER(A1)` | Returns the value in A1 in upper case |
| `=PROPER(A1)` | Returns the value in A1 in proper case (e.g. "hello world" → "Hello World") |
| `=TRIM(A1)` | Returns the value in A1 with all leading and trailing spaces removed |
| `=SUBSTITUTE(A1, " ", "")` | Returns the value in A1 with all spaces removed |

> **Note:** Google Sheets and Excel have many more functions than the ones listed above.

---

### Absolute References

| Reference Type | Description |
|---------------|-------------|
| `$A$1` | Absolute reference (does not change when copied) |
| `$A1` | Absolute column, relative row (column remains fixed) |
| `A$1` | Relative column, absolute row (row remains fixed) |

> **Note:** Absolute references are useful for referencing fixed values (e.g. constants).  
> **Beware:** `$A1` keeps the column fixed while allowing row changes, whereas `A$1` keeps the row fixed while allowing column changes.

---

### Conditional Formatting

| Step | Description |
|------|-------------|
| 1 | Select the cells you want to apply conditional formatting to |
| 2 | Click on the "Format" menu and select "Conditional formatting" |
| 3 | Select the type of conditional formatting (e.g. "Greater than") |
| 4 | Enter the value you want to compare the cell to (e.g. `10`) |
| 5 | Select the style you want to apply (e.g. "Bold") |
| 6 | Click on "Done" |

---

### Insert Chart

| Step | Description |
|------|-------------|
| 1 | Select the cells you want to include in the chart |
| 2 | Click on the "Insert" menu and select "Chart" |
| 3 | Select the type of chart you want (e.g. "Column chart") |
| 4 | Style the chart as needed |
| 5 | Add x-axis data if required |

---

### Split Column Text to Multiple Columns

| Step | Description |
|------|-------------|
| 1 | Select the column you want to split |
| 2 | Click on the "Data" menu and select "Split text to columns" |
| 3 | Select the separator (e.g. "Space") |

> **Example:** "John Doe" will be split into "John" and "Doe" in separate columns.

---

### Extract Text from a Cell

| Function | Description |
|----------|-------------|
| `=LEFT(A1, 5)` | Returns the first 5 characters from the `A1` cell |
| `=RIGHT(A1, 5)` | Returns the last 5 characters from the `A1` cell |
| `=MID(A1, 5, 10)` | Returns 10 characters from the `A1` cell starting from the 5th character |

> **Note:** Indexing starts at **1**, not **0** like in many programming languages.

---

### Fill Down

Sometimes you want to fill down a column with the same value or formula

#### Method 1

- Select the cell you want to fill down
- Click and hold the bottom right corner of the cell (the cursor should change to a cross)
- Drag the cell down to the last cell you want to fill down

#### Method 2

- Select the cell you want to fill down
- Hold down the `shift` key and press `down arrow` (or click on the last cell you want to fill down)
- Click `cmd + d` to fill down the column

---

### Sort

You can sort selected cells, columns, rows or the entire sheet

- Select the cells, columns, rows or the entire sheet you want to sort (e.g. click on the top left square to select the entire sheet)
- Click on the "Data" menu and select "Sort range" -> "Advanced range sorting options"
- If the sheet has a header row, check the "Data has header row" checkbox
- Select the column you want to sort by
- Select the order you want to sort by (e.g. "A to Z")
- Click on the "Sort" button

---

### Filter

You can filter selected cells, columns, rows or the entire sheet

#### Create a filter vs Filter Views

- **Filter views**: The filter will be applied to the sheet and will be visible only to you
- **Create a filter**: The filter will be applied to the sheet and will be visible to everyone who has access to the sheet

#### Filter views

- Click on the "Data" menu and select "Filter views" -> "Create new filter view"
- Select the column you want to filter by
- Select the condition you want to filter by (e.g. "Greater than")
- Enter the value you want to filter by (e.g. 10)
- Click on the "OK" button
- Choose a name for the filter view (e.g. "Only sales from Arizona")

---

### Pivot Table

A Pivot Table allows you to summarize data from a table into a new table

- Select the cells you want to include in the pivot table
- Click on the "Insert" menu and select "Pivot table"

> Note: A new sheet will be created with the pivot table

- Go to the "Pivot table editor" section on the right
- Select either the suggested pivot table or create your own by selecting the columns, rows, values or filters you want to include in the pivot table
- Click on the "Add" button

> TIP: You can then insert a chart based on the pivot table

---

### Lookup Table

A lookup table allows you to lookup a value in a table and return a value from another column in the same row

- Create a table with the values you want to lookup:

> Note: Those are simply two columns with values that you can put anywhere in the sheet

| B   | C        |
| --- | -------- |
| CR  | Chrysler |
| FD  | Ford     |

- Sort the table by the first column (e.g. "B"), if not the sorted, the lookup will not work

> See [Sort](#sort)

- Select the new cell you want to return the value to
- Enter the formula `=VLOOKUP(A1, B$1:C$2, 2)`

> Note: `A1` is the value you want to lookup (which in this case is placed in the A column), `B$1:C$2` is the table you want to lookup the value in, `2` is the lookup table column number you want to return the value from
>
> We used an absolute reference for the table because we want to be able to copy the formula to other cells

---

### General Tips

- You can use the `=` operator to convert a value to a number (e.g. `=A1*2`)
- You can click on a column header to select the entire column
- You can add a column by right clicking on a column header and selecting "Insert 1 left"
- You can calculate the number of days between two dates by subtracting them (e.g. `=A1-A2`)
- Double click on the column right border to auto resize the column to fit the content
- You can rotate text in a cell by selecting the cell and then clicking on the "Text Rotation" button in the toolbar
- You can either use `.5` or `50%` to represent 50%