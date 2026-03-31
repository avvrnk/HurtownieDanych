# Zdefiniowane KPI 
### 1. Wzrost liczby opracowanych i opublikowanych ofert wycieczek zagranicznych na poziomie nie mniejszym niż 0,5% miesięcznie w porównaniu z danym miesiącem w poprzednim roku. 
##### Nazwa 
```
Wzrost liczby ofert 
```
##### Value Expression 
```
[Measures].[Oferta Count]
```
##### Goal Expression
```
([Measures].[Oferta Count],
ParallelPeriod(
    [Data].[Hierarchia daty wyjazdu].[Rok],
    1,
    [Data].[Hierarchia daty wyjazdu].CurrentMember
))*1.005

```
##### Status Expression
```
IIF(
    KPIValue("Wzrost liczby ofert"),
    1,
    IIF(
        KPIValue("Wzrost liczby ofert") >= KPIGoal("Wzrost liczby ofert")*0.998,
        0.5,
        -1
    )
)
```
##### Trend Expression
```
IIF(
    KPIValue("Wzrost liczby ofert") > (
        KPIValue("Wzrost liczby ofert"),
        ParallelPeriod(
            [Data].[Hierarchia daty wyjazdu].[Rok],
            1,
            [Data].[Hierarchia daty wyjazdu].CurrentMember
            )
        ),
    1,
    -1
)
```
### 2. Wzrost liczby wycieczek niemniejszy niż 10% w co najmniej 3 krajach, w których w poprzednim roku liczba ofert wyjazdów była najmniejsza.
##### Nazwa 
```
Wzrost liczby ofert w kraju
```
##### Value Expression 
```
[Measures].[Oferta Count]
```
##### Goal Expression
```
([Measures].[Oferta Count],
ParallelPeriod(
    [Data].[Hierarchia daty wyjazdu].[Rok],
    1,
    [Data].[Hierarchia daty wyjazdu].CurrentMember
))*1.005
```
##### Status Expression
```
IIF(
    KPIValue("Wzrost liczby ofert w kraju"),
    1,
    IIF(
        KPIValue("Wzrost liczby ofert w kraju") >= KPIGoal("Wzrost liczby ofert w kraju")*0.998,
        0.5,
        -1
    )
)
```
##### Trend Expression
```
IIF(
    KPIValue("Wzrost liczby ofert w kraju") > (
        KPIValue("Wzrost liczby ofert w kraju"),
        ParallelPeriod(
            [Data].[Hierarchia daty wyjazdu].[Rok],
            1,
            [Data].[Hierarchia daty wyjazdu].CurrentMember
            )
        ),
    1,
    -1
)
```
### 3. Średnie obłożenie ofert w ujęciu miesięcznym 
##### Nazwa 
```
Srednie oblozenie ofert 
```
##### Value Expression 
```
[Measures].[OblozenieAVG]
```
##### Goal Expression
```
0.75
```
##### Status Expression
```
IIf( 
    KPIValue("Srednie oblozenie ofert") >= KPIGoal("Srednie oblozenie ofert"),
    1,
    IIf(
        KPIValue("Srednie oblozenie ofert") >= KPIGoal("Srednie oblozenie ofert")*0.998, 
        0.5, 
        -1
    )
)
```
##### Trend Expression
```
IIf( 
    KPIValue("Srenie oblozenie ofert") > (
        KPIValue("Srednie oblozenie"), 
        ParallelPeriod(
            [Data].[Hierarchia daty wyjazdu].[Rok],
            1,
            [Data].[Hierarchia daty wyjazdu].CurrentMember
            )
        ),
    1,
    -1
)
```
# Zapytania MDX  
### 1. Które kierunki wycieczek osiągnęły najwyższy poziom wykorzystania miejsc (powyżej 75%)?  
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS,  
    Filter( 
        [Wycieczka].[Kraj].Children, 
        [Measures].[OblozenieAVG] > 0.75
    ) ON ROWS 
FROM [Trip Out DW]; 
```
### 2. Jaka jest zależność między kategorią cenową wycieczki a poziomem rezerwacji (czy krótsze pobyty sprzedają się lepiej)? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    [Wycieczka].[Cena Kat].Children ON ROWS 
FROM [Trip Out DW]; 
```
### 3. Które terminy wyjazdów (miesiące lub sezony) generują największe zainteresowanie klientów? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    Order( 
        [Data].[Miesiac].Children, 
        [Measures].[OblozenieAVG], 
        DESC 
    ) ON ROWS 
FROM [Trip Out DW]; 
```
### 4. Czy typ wycieczki “objazdowa” sprzedaje się częściej niż inne typy wycieczek? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    Filter(
    [Wycieczka].[Typ Wycieczki].Children,
    [Wycieczka].[Typ Wycieczki].CurrentMember.Name ="objazdowa"
    ) ON ROWS 
FROM [Trip Out DW];
```
### 5. Czy oferty z pełnym wyżywieniem sprzedają się częściej niż oferty bez wyżywienia lub ze śniadaniami? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT 
    [Measures].[OblozenieProcent] ON COLUMNS, 
    [Hotel].[Zakres Wyzywienia].Children ON ROWS 
FROM [Trip Out DW]; 
```
### 6. Jakie udogodnienia występują najczęściej w hotelach o najwyższym poziomie wypełnienia miejsc (powyżej 75%)? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    Filter( 
        [Hotel].[Udogodnienie Glowne].Children, 
        [Measures].[OblozenieAVG] > 0.75
    ) ON ROWS 
FROM [Trip Out DW]; 
```
### 7. Jakie typy pokoi występują najczęściej w hotelach o najwyższym poziomie wypełnienia miejsc (powyżej 80%)? 
```
WITH
    MEMBER [Measures].[LPokoi2osSUM] AS
            VAL([Hotel].[Id Hotelu].CurrentMember.Properties("L Pokoi2os"))

    MEMBER [Measures].[LPokoi3osSUM] AS
            VAL([Hotel].[Id Hotelu].CurrentMember.Properties("L Pokoi3os"))

    MEMBER [Measures].[LPokoi4osSUM] AS
            VAL([Hotel].[Id Hotelu].CurrentMember.Properties("L Pokoi4os"))

SELECT
    {
        [Measures].[LPokoi2osSUM],
        [Measures].[LPokoi3osSUM],
        [Measures].[LPokoi4osSUM], 
        [Measures].[OblozenieAVG]
    } ON COLUMNS, 
    FILTER(
        [Hotel].[Id Hotelu].Members,
        [Measures].[OblozenieAVG] > 0.8
    ) ON ROWS
FROM [Trip Out DW]

```
### 8. Czy oferty z hotelami o wyższym standardzie mają wyższy poziom wypełnienia miejsc?
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    Order( 
        [Hotel].[Standard Hotelu].Children, 
        [Measures].[OblozenieAVG], 
        DESC 
    ) ON ROWS 
FROM [Trip Out DW]; 
```
### 9. Które hotele były najczęściej wykorzystywane w ofertach, które uzyskały najwyższy poziom rezerwacji? 
```
WITH  
    MEMBER [Measures].[OblozenieProcent] AS  
        [Measures].[OblozenieAVG] * 100 
SELECT  
    [Measures].[OblozenieProcent] ON COLUMNS, 
    TopCount(
        Filter( 
            [Hotel].[BK Hotelu].Children,  
            [Measures].[OblozenieAVG] > 0.8
        ), 
        10, 
        [Measures].[OblozenieAVG] 
    ) ON ROWS 
FROM [Trip Out DW]; 
```
### 10. Jakie jest średnie obłożenie miejsc w zależności od zakresu wyżywienia w hotelu? 
```
WITH   
    MEMBER [Measures].[OblozenieProcent] AS   
        [Measures].[OblozenieAVG] * 100  
    MEMBER [Measures].[SrednieOblozenieProcent] AS 
        AVG( 
            NONEMPTY(
                [Hotel].[BK Hotelu].Members, 
                ([Hotel].[Zakres Wyzywienia].CurrentMember, [Measures].[OblozenieProcent]) 
            ), 
            ([Hotel].[Zakres Wyzywienia].CurrentMember, [Measures].[OblozenieProcent]) 
        ) 
SELECT  
    [Measures].[SrednieOblozenieProcent] ON COLUMNS,  
    [Hotel].[Zakres Wyzywienia].Members ON ROWS  
FROM [Trip Out DW]; 
```
### 11. Jakie miesiące w roku 2024 osiągnęły najwyższy poziom obłożenia dla ofert obejmujących hotele o standardzie czterogwiazdkowym? 
```
WITH   
    MEMBER [Measures].[OblozenieProcent] AS   
        [Measures].[OblozenieAVG] * 100  
SELECT 
    [Measures].[OblozenieProcent] ON COLUMNS, 
    Descendants(
        [Data].[Hierarchia daty wyjazdu].[Rok].&[2024], 
        [Data].[Hierarchia daty wyjazdu].[Miesiac]
    ) ON ROWS 
FROM [Trip Out DW]
WHERE ([Hotel].[Standard Hotelu].&[4]); 
```
