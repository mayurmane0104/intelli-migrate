# Creating maps and geospatial charts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/geospatial-charts.html](https://docs.aws.amazon.com/quick/latest/userguide/geospatial-charts.html)

---

You can create two types of maps in Quick: point maps and filled maps.
				*Point maps* show the difference between data
			values for each location by size. *Filled maps* show
			the difference between data values for each location by varying shades of color.

###### Important

Geospatial charts in Quick currently aren't supported in some AWS Regions, including in China.

For help with geospatial issues, see [Geospatial troubleshooting](./geospatial-troubleshooting.html).

Before you get started creating maps, do the following:

- 
				Make sure that your dataset contains location data. *Location data*is data that corresponds to latitudinal and longitudinal values. Location data can include a column for latitude and a column for longitude in your dataset. It can also include a column with city names. Quick can chart latitude and longitude coordinates. It also recognizes geographic components such as country, state or region, county or district, city, and ZIP code or postal code.
- 
				Make sure that your location data fields are marked as geospatial data types. 
- 
				Consider creating geographic hierarchies. 

For more information about working with geospatial data, including changing field data
			types and creating geospatial hierarchies, see [Adding geospatial data](./geospatial-data-prep.html).

To learn more about creating maps in Quick, see the following.