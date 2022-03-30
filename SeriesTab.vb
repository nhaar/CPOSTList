Sub MainTab()
    Range("A1:J1").Select
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
    Selection.Delete Shift:=xlToLeft
    No_rows = Cells(Rows.Count, 3).End(xlUp).Row
    Dim j As Integer
        For j = 2 To No_rows
            If Len(Range("C" + CStr(j)).Value) > 3 Then
            Text = Range("C" + CStr(j)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Range("B" + CStr(j)), Address:= _
            Text
            End If
            Next j
    Columns("C:C").Select
    Selection.Delete Shift:=xlToLeft
    No_rows = Cells(Rows.Count, 5).End(xlUp).Row
    Dim k As Integer
        For k = 2 To No_rows
            If Len(Range("E" + CStr(k)).Value) > 3 Then
            Range("E" + CStr(k)).Select
            Text = Range("E" + CStr(k)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:= _
                Text, TextToDisplay:="Link"
            End If
            Next k
    Columns("A:A").ColumnWidth = 32.43
    Columns("C:C").ColumnWidth = 5.43
    Columns("G:G").ColumnWidth = 12.43
    Columns("H:H").ColumnWidth = 23.86
    Columns("D:D").ColumnWidth = 25.86
    Columns("F:F").ColumnWidth = 26.43
    Columns("F:F").ColumnWidth = 37.29
    Columns("H:H").ColumnWidth = 37.86
    Columns("B:B").ColumnWidth = 31.29
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
    Columns("G:G").Select
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
    Range("G1").Select
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