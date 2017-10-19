//Binar Insert Sort by Kuznetsov
program Project1;

{$APPTYPE CONSOLE}

uses
  SysUtils;

type
   TMyArray = array[0..100000] of integer;
   TimeArray = array[0..2] of tdatetime;
   StackArray = array [0..2] of integer;
   TRec = record
      N: Integer;
      Name : string;
      Lastname : string;
      Age : integer;
      Weight: integer;
   end;
   TAddArray = array[0..100000] of TRec;

   AlgSort = function(var Mas:TMyArray;N:integer):TMyArray; //not use
var
   M:TMyArray;
   M2:TAddArray; //Изменения v2.0
   stack: StackArray = (1000,10000,100000);
   timeRand:TimeArray;
   timeSort:TimeArray;
   timeRevSort:TimeArray;
   i,j:integer;

procedure  BinarInsert(var Mas:TMyArray;N:integer);
  var
    i,j,temp,left,right,m:integer;
  begin
    for i:= 1 to N-1  do
      begin
        temp:= Mas[i];
        left:= 0;
        right:= i-1;
        while left<=right do
           begin
                 m:= (left+right) div 2;
                 if temp<Mas[m] then
                       right:= m-1
                 else
                       left:= m+1;
           end;
        for j:=i-1 downto left do
             Mas[j+1]:=Mas[j];
        Mas[left]:=temp;
       end;
   end;

//Изменения v2.0
procedure BinarInsert2(var Mas:TAddArray;S:integer);
  var
    i,j,left,right,m,temp:integer;
    temp2:TRec;
  begin
    for i:= 1 to S-1  do
      begin
        temp:= Mas[i].N;
        temp2:=Mas[i];
        left:= 0;
        right:= i-1;
        while left<=right do
           begin
                 m:= (left+right) div 2;
                 if temp<Mas[m].N then
                       right:= m-1
                 else
                       left:= m+1;
           end;
        for j:=i-1 downto left do
             Mas[j+1]:=Mas[j];
        Mas[left]:=temp2;
       end;
  end;

function Times(var Mas:TMyArray;N:integer):tdatetime;
  var
      t1, t2: tdatetime;
  begin
      t1:=now;
      BinarInsert(Mas,N);       //Работа только с бинарными вставками Part1
      t2:=now;
      result:=t2-t1;
  end;

function Times2(var Mas:TAddArray;N:integer):tdatetime;
  var
      t1, t2: tdatetime;
  begin
      t1:=now;
      BinarInsert2(Mas,N);       //Работа только с бинарными вставками Part2
      t2:=now;
      result:=t2-t1;
  end;

procedure Table(var stack:StackArray;timeSort:TimeArray;timeRand:TimeArray;timeRevSort:TimeArray);
  var
     i:integer;
  begin
     writeln('-----------------------------------------------------------------------');
     writeln('| N |Elements qt. |Time(Sort(mas))| Time(Rand(mas))|Time(reverse(mas))|');
     writeln('-----------------------------------------------------------------------');
     for i:=0 to length(stack)-1 do
       begin
         writeln('|'+Format('%3d',[i+1])+'|'+
            Format('%13d', [stack[i]])+'|'+
            Format('%15s',[FormatFloat('0.###',timeSort[i]*24*60*60)])+'|'+
               Format('%16s',[FormatFloat('0.###',timeRand[i]*24*60*60)])+'|'+
                  Format('%18s',[FormatFloat('0.###',timeRevSort[i]*24*60*60)])+'|');
         writeln('-----------------------------------------------------------------------');
       end;
  end;

procedure ReverseArr(var Mas:TMyArray;N:integer);
   var
     i,T:integer;
   begin
     for i:=0 to ((N-1) div 2) do
       begin
          T:=Mas[i];
          Mas[i]:=Mas[N-i-1];
          Mas[N-i-1]:=T;
       end;
   end;

procedure ReverseArr2(var Mas:TAddArray;N:integer);
   var
     i:integer;
     T:TRec;
   begin
     for i:=0 to (N-1) div 2 do
       begin
          T:=Mas[i];
          Mas[i]:=Mas[N-i-1];
          Mas[N-i-1]:=T;
       end;
   end;

begin
   writeln('Binar Insert Sort');
   //Part 1
   writeln('Part 1');
   for i := 0 to length(stack)-1 do
        begin
           for j := 0 to stack[i]-1 do
              M[j]:=trunc(random(1000-(-1000)+1)-1000);
           timeRand[i]:=Times(M,stack[i]);
           timeSort[i]:=Times(M,stack[i]);
           ReverseArr(M,stack[i]);
           timeRevSort[i]:=Times(M,stack[i]);
        end;
   Table(stack,timeSort,timeRand,timeRevSort);
   //Part 2
   writeln('Part 2');
   for i := 0 to length(stack) - 1 do
      begin
         for j := 0 to stack[i] - 1 do
             begin
                 M2[j].N := trunc(random(1000-(0)+1)-0);
                 M2[j].Name := chr(trunc(random(64-128+1)-64));
                 M2[j].Lastname:=  chr(trunc(random(64-128+1)-64));
                 M2[j].Age := trunc(random(100-(1)+1)-1);
                 M2[j].Weight := random((230-(1)+10)-10);
             end;
           timeRand[i]:=Times2(M2,stack[i]);
           timeSort[i]:=Times2(M2,stack[i]);
           ReverseArr2(M2,stack[i]);
           timeRevSort[i]:=Times2(M2,stack[i]);
      end;
   Table(stack,timeSort,timeRand,timeRevSort);
   readln;
end.
