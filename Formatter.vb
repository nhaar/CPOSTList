Sub SeriesFormat()
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
    No_rows = Cells(Rows.Count, 6).End(xlUp).Row
    Dim j As Integer
        For j = 2 To No_rows
            If Len(Range("F" + CStr(j)).Value) > 3 Then
            Text = Range("F" + CStr(j)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Range("E" + CStr(j)), Address:= _
            Text
            End If
            Next j
    Columns("F:F").Select
    Selection.Delete Shift:=xlToLeft
    No_rows = Cells(Rows.Count, 4).End(xlUp).Row
    Dim k As Integer
        For k = 2 To No_rows
            If Len(Range("D" + CStr(k)).Value) > 3 Then
            Range("D" + CStr(k)).Select
            Text = Range("D" + CStr(k)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:= _
                Text, TextToDisplay:="Link"
            End If
            Next k
    Columns("A:A").ColumnWidth = 32.43
    Columns("C:C").ColumnWidth = 8.43
    Columns("G:G").ColumnWidth = 23.86
    Columns("H:H").ColumnWidth = 13.86
    Columns("D:D").ColumnWidth = 4.57
    Columns("F:F").ColumnWidth = 26.43
    Columns("F:F").ColumnWidth = 37.29
    Columns("H:H").ColumnWidth = 37.86
    Columns("B:B").ColumnWidth = 25.86
    Columns("E:E").ColumnWidth = 31.29
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
    Columns("H:H").Select
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
    Range("H1").Select
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
Sub MediaFormat()
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
    No_rows = Cells(Rows.Count, 8).End(xlUp).Row
    Dim j As Integer
        For j = 2 To No_rows
            If Len(Range("H" + CStr(j)).Value) > 3 Then
            Text = Range("H" + CStr(j)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Range("G" + CStr(j)), Address:= _
            Text
            End If
            Next j
    Columns("H:H").Select
    Selection.Delete Shift:=xlToLeft
    No_rows = Cells(Rows.Count, 4).End(xlUp).Row
    Dim k As Integer
        For k = 2 To No_rows
            If Len(Range("D" + CStr(k)).Value) > 3 Then
            Range("D" + CStr(k)).Select
            Text = Range("D" + CStr(k)).Value
            ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:= _
                Text, TextToDisplay:="Link"
            End If
            Next k
    Columns("A:A").ColumnWidth = 32.43
    Columns("C:C").ColumnWidth = 8.43
    Columns("G:G").ColumnWidth = 31.29
    Columns("H:H").ColumnWidth = 13.86
    Columns("D:D").ColumnWidth = 4.57
    Columns("F:F").ColumnWidth = 26.43
    Columns("F:F").ColumnWidth = 37.29
    Columns("H:H").ColumnWidth = 13.86
    Columns("B:B").ColumnWidth = 25.86
    Columns("E:E").ColumnWidth = 23.86
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
    Columns("H:H").Select
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
    Range("H1").Select
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