Sub SideTab()
    Range("A1:I1").Select
    Selection.Font.Bold = True
    No_Of_Rows = Cells(Rows.Count, 1).End(xlUp).Row
    Dim i As Integer
        For i = 2 To No_Of_Rows
            If Range("B" + CStr(i)).Value = 1 Then
            Range("A" + CStr(i)).Select
            Selection.Font.Color = RGB(46, 71, 170)
            Else
            Range("A" + CStr(i)).Select
            Selection.Font.Color = RGB(204, 0, 0)
            End If
            Next i
	Columns("B:B").Select
    Selection.delete Shift:=xlToLeft
	Columns("A:A").ColumnWidth = 36
    Columns("B:B").ColumnWidth = 5.80
    Columns("C:C").ColumnWidth = 12.57
    Columns("E:E").ColumnWidth = 63.86
    Columns("C:C").Select
    With Selection
        .HorizontalAlignment = xlRight
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Range("C1").Select
    With Selection
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
	Columns("A:A").Select
    With Selection
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlBottom
        .WrapText = False
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
End Sub