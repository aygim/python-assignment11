import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

# df['strength'] = df['strength'].str.replace('0-1', '0.5')
# df['strength'] = df['strength'].str.replace('+', '')
# df['strength'] = df['strength'].astype(float)


# def convert_strength(value):
#     if '-' in value:
#         parts = value.split('-')
#         return (float(parts[0]) + float(parts[1])) / 2  
#     elif '+' in value:
#         return float(value.replace('+', '')) 
#     else:
#         return float(value)  
# df['strength'] = df['strength'].apply(convert_strength)


df['strength'] = df['strength'].str.replace(r'(\d+)-(\d+)', lambda m: str((int(m.group(1)) + int(m.group(2))) / 2), regex=True)
df['strength'] = df['strength'].str.replace('+', '', regex=False)

df['strength'] = df['strength'].astype(float)

print("\n After conversion")
print(df.head(10))
print(df.tail(10))


fig = px.scatter(df, x='frequency', y='strength', color='direction',
                 title='Wind Strength vs Frequency')
fig.write_html("wind.html")
fig.show()