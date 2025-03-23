if you want to try, just run the "Well Predict.ipynb"

Logs Data 
df (Logs Data) 

for logs data you need to make sure your data is on format .Las 
and the data needs a menemonics such as,

GR    --> Gamma Ray (API Format),

RHOB  --> Density   (g/cc),

DT    --> P-Wave    (us/ft),

LLD   --> Deep Resistivity  (ohm.m),

NPHI  --> Neutron Porosity  (v/v)

Tops Data
df2 (Tops Data)

Tops data were additional, if there is no tops data then just make the line into a comment line.
if you have a Tops Data, then you must make sure the data was on .txt type and the format data was
Top  |  Bottom | Fm

Top      --> Top of Formation

Bottom   --> Bottom of Formation

Fm       --> Formation Name

on script 
from well_display import * ( it's contain several well plot design )
df (Logs Data) , df2 (Tops Data)

- plot_general_logs(df)    --> General Triple Combo Plot ,
- 
- plot_well_logs1(df)      --> General Triple Combo Plot + ( Vp, Acoustic Impedance, and Coeffiicient Refflection),
- 
- plot_well_logs2(df, df2) --> General Triple Combo Plot + ( Vp, Acoustic Impedance, and Coeffiicient Refflection) + Tops Plot,
- 
- plot_well_logs3(df)      --> Petophysical Evaluation and Litho-Fluid Prediction Result Plot,
- 
- plot_well_logs4(df, df2) --> Petophysical Evaluation and Litho-Fluid Prediction Result Plot + Tops Plot,
