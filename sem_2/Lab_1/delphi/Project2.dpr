program Project2;

{$APPTYPE CONSOLE}

uses
  SysUtils;

   const n=12;m=7;
 type Sarray=array[1..n,0..m] of real;
 type Yarray=array[1..n] of real;


var S1:Sarray;
    Y1:Yarray;
  var i,j,A,B,imax,k:integer;
  var max,cash,temp:real;

procedure input(var S:Sarray;a,b:integer);
  begin
      writeln('Ввод матрицы по 1му элементу в строке');
      for i := 1 to a do
        for j := 1 to b do
           readln(S[i,j]);
  end;

procedure action(S:Sarray; var Y:Yarray; a,b:integer);
  begin
     //заполнение массива Y
     k:=1;
     for j := 1 to B  do begin
      temp:=0;
      for i := 1 to A do
        if S[i,j]>0 then
          temp:=temp+S[i,j];
      if temp>0 then begin
        Y[k]:=temp/A;
        k:=k+1;
      end;
     end;
    //Нахождение номера макс.элем. и перестановка элем.мас.Y
     max:=0;
     cash:=0;
     for i := 1 to k-1 do
      if Y[i]>max then begin
        max:=Y[i];
        imax:=i;
      end;

     cash:=Y[imax];
     Y[imax]:=Y[k-1];
     Y[k-1]:=cash;
  end;

procedure output( S:Sarray; Y:Yarray;a,b:integer);
  begin
     //matrix S
    writeln('Результат выполнения программы:');
    writeln;
    writeln('Матрица S:');
    for i := 1 to A do begin
       for j := 1 to B  do
          write(S[i,j]:6:3,'  ');
       writeln;
    end;
    //massiv Y
    writeln('Вектор Y: ');
    writeln;
    for i := 1 to k-1 do
       write(Y[i]:6:3,' ');
    writeln;
  end;
begin
    writeln('Введите количество строк: ');
    readln(A);
    writeln('Введите количество столбцов: ');
    readln(B);
    if (A<=12) and (A>=1) and (B<=7) and (B>=1) then
     begin
       input(S1,A,B);
       action(S1,Y1,A,B);
       output(S1,Y1,A,B);
       readln;
     end
     else writeln('Указаны неверные границы матрицы');
    readln;
end.
