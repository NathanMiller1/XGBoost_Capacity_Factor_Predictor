import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data to pandas dataframe
df_plant_data = pd.read_csv('solar.csv')
#df_plant_data = pd.read_csv('wind.csv')

#df_plant_data = df_plant_data.loc[(df_plant_data['x']>0) | (df_plant_data['y']>0)]
#df_plant_data.loc[11182, 'x'] = df_plant_data['x'].median()
#df_plant_data.loc[11182, 'z'] = df_plant_data['z'].median()
#df_plant_data = df_plant_data.loc[~((df_plant_data['y'] > 30) | (df_plant_data['z'] > 30))]
#df_plant_data = pd.concat([df_plant_data, pd.get_dummies(df_plant_data['cut'], prefix='cut', drop_first=True)], axis=1)
#df_plant_data = pd.concat([df_plant_data, pd.get_dummies(df_plant_data['color'], prefix='color', drop_first=True)], axis=1)
#df_plant_data = pd.concat([df_plant_data, pd.get_dummies(df_plant_data['clarity'], prefix='clarity', drop_first=True)], axis=1)


numerical_features = ['avg_air_temperature', 'avg_alpha', 'avg_aod', 'avg_asymmetry', 'avg_cld_opd_dcomp',
                      'avg_cld_reff_dcomp', 'avg_clearsky_dhi',	'avg_clearsky_dni',	'avg_clearsky_ghi',
                      'avg_cloud_press_acha', 'avg_cloud_type', 'avg_dew_point', 'avg_dhi', 'avg_dni', 'avg_ghi',
                      'avg_ozone', 'avg_relative_humidity', 'avg_solar_zenith_angle', 'avg_ssa', 'avg_surface_albedo',
                      'avg_surface_pressure', 'avg_total_precipitable_water', 'avg_wind_direction', 'avg_wind_speed',
                      'std_air_temperature', 'std_alpha', 'std_aod', 'std_asymmetry', 'std_cld_opd_dcomp',
                      'std_cld_reff_dcomp', 'std_clearsky_dhi', 'std_clearsky_dni',	'std_clearsky_ghi',
                      'std_cloud_press_acha', 'std_cloud_type', 'std_dew_point', 'std_dhi', 'std_dni', 'std_ghi',
                      'std_ozone', 'std_relative_humidity', 'std_solar_zenith_angle', 'std_ssa', 'std_surface_albedo',
                      'std_surface_pressure', 'std_total_precipitable_water', 'std_wind_direction', 'std_wind_speed',
                      'wind_u5', 'wind_5_10', 'wind_10_15', 'wind_15_20', 'wind_20_25', 'wind_o25', 'temp_u0',
                      'temp_0_10', 'temp_10_20', 'temp_20_30', 'temp_30_40', 'temp_o40', 'wind_power_density']

"""
def desc_num_feature(feature_name, bins=30, edgecolor='k', **kwargs):
    fig, ax = plt.subplots(figsize=(8,4))
    df_plant_data[feature_name].hist(bins=bins, edgecolor=edgecolor, ax=ax, **kwargs)
    ax.set_title(feature_name, size=15)
    plt.figtext(1,0.15, str(df_plant_data[feature_name].describe().round(2).astype(str)), size=17)
    plt.savefig('chart.png')
"""
#desc_num_feature('avg_air_temperature')

# TODO: save charts for all numerical features
#for x in numerical_features:
#    desc_num_feature(x)

sns.pairplot(df_plant_data[numerical_features], plot_kws={"s": 2});
plt.savefig('chart.png')