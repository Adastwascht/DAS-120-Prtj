import xarray as xr
import zipfile as zp

with zp.ZipFile("C:/Users/Hegemon/Desktop/DSA 210 Project/yearly_weather_data_med.nc", "r") as z:
    z.extractall("C:/Users/Hegemon/Desktop/DSA 210 Project")


ds_a = xr.open_dataset("C:/Users/Hegemon/Desktop/DSA 210 Project/Finalized Data/data_stream-moda_stepType-avgua.nc")
ds_b = xr.open_dataset("C:/Users/Hegemon/Desktop/DSA 210 Project/Finalized Data/data_stream-moda_stepType-avgad.nc")

df_a = ds_a.to_dataframe().reset_index()
df_b = ds_b.to_dataframe().reset_index()

df_a.to_csv("uncleaned temp-wind data era5.csv", index=False)
df_b.to_csv("uncleaned precipitation data era5.csv", index=False)