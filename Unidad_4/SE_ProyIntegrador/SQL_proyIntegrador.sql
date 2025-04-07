--PASO 1
CREATE DATABASE [BD_PROY_INTEGRADO_SE]

--PASO 2
CREATE TABLE [dbo].[sensor_info](
    [id_sensor] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
    [name] [nvarchar](100) NOT NULL,     
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[sensor_info] ADD PRIMARY KEY CLUSTERED 
(
    [id_sensor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]


INSERT INTO sensor_info (NAME) VALUES('SENSOR DE DISTANCIA')
INSERT INTO sensor_info (NAME) VALUES('SENSOR DE VELOCIDAD')

SELECT * FROM sensor_info


--PASO 3

CREATE TABLE [dbo].[sensor_records](
    [id_record] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
    [id_sensor] [numeric](18, 0) NOT NULL,
    [current_value] [numeric](18, 0) NOT NULL,
    [date_record] [datetime] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[sensor_records] ADD PRIMARY KEY CLUSTERED 
(
    [id_record] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

--PASO 4
CREATE PROCEDURE [dbo].[SP_Insert_SensorRecords] 
    -- Add the parameters for the stored procedure here
    @id_sensor as numeric(18,0), 
    @current_value as numeric(18,0)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[sensor_records]
           ([id_sensor]
            ,[date_record]
            ,[current_value]
           )
     VALUES
           (@id_sensor
            ,GETDATE()
           ,@current_value
           )
    
END


---PASO 5
exec SP_Insert_SensorRecords 1, 120
exec SP_Insert_SensorRecords 1, 240
exec SP_Insert_SensorRecords 1, 170
exec SP_Insert_SensorRecords 1, 390
exec SP_Insert_SensorRecords 2, 80
exec SP_Insert_SensorRecords 2, 140
exec SP_Insert_SensorRecords 2, 890

select * from sensor_records

CREATE PROCEDURE [dbo].[SP_SelectALL_records]
    -- Add the parameters for the stored procedure here 
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT SI.id_sensor, SI.name "NAME", SR.current_value "CURRENT_VALUE", SR.date_record "DATE_RECORD"
    FROM sensor_records SR
    INNER JOIN sensor_info SI ON SR.id_sensor = SI.id_sensor        
           
END


CREATE PROCEDURE [dbo].[SP_SelecLastRecordByID]
    -- Add the parameters for the stored procedure here 
    @id_sensor as numeric(18,0)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT top 1 SI.id_sensor, SI.name "NAME", SR.current_value "CURRENT_VALUE", SR.date_record "DATE_RECORD"
    FROM sensor_records SR
    INNER JOIN sensor_info SI ON SR.id_sensor = SI.id_sensor        
    where SI.id_sensor = @id_sensor
    order by SR.date_record desc
           
END


SP_SelecLastRecordByID 2


--PASO 6
CREATE TABLE [dbo].[toma_decisiones](
    [id_decision] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
    [velocidad] [numeric](18, 0) NOT NULL,
    [distancia] [numeric](18, 0) NOT NULL,
    [decision] [numeric](18, 0) NOT NULL,
    [date_record] [datetime] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[toma_decisiones] ADD PRIMARY KEY CLUSTERED 
(
    [id_decision] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]


--paso 7
CREATE PROCEDURE [dbo].[SP_Insert_Decision] 
    -- Add the parameters for the stored procedure here        
    @velocidad as numeric(18, 0),
    @distancia as numeric(18, 0),
    @decision as numeric(18, 0)  
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[toma_decisiones]
           ([velocidad]
            ,[distancia]
            ,[decision],
            [date_record]
           )
     VALUES
           (@velocidad,
           @distancia,
           @decision
            ,GETDATE()           
           )
    
END


SP_Insert_Decision 10, 20, 1
SP_Insert_Decision 20, 40, 2
SP_Insert_Decision 60, 60, 3

select * from toma_decisiones

--paso 8
CREATE PROCEDURE [dbo].[SP_SelecLastDecision]
    -- Add the parameters for the stored procedure here   
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT top 1 *
    FROM toma_decisiones        
    order by date_record desc
           
END