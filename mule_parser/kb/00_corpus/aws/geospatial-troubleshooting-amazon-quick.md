# Geospatial troubleshooting - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/geospatial-troubleshooting.html](https://docs.aws.amazon.com/quick/latest/userguide/geospatial-troubleshooting.html)

---

Use this section to discover the Amazon Quick Sight requirements for correctly processing geospatial data. If Amazon Quick Sight doesn't recognize your geospatial data as geospatial, use this section to help troubleshoot the issue. Make sure that your data follows the guidelines listed, so that it works in geospatial visuals.

###### Note

Geospatial charts in Amazon Quick Sight currently aren't supported in some AWS Regions, including in China. We are working on adding support for more Regions.

If your geography follows all the guidelines listed here, and still generates errors, contact the Amazon Quick Sight team from within the Amazon Quick Sight console.

###### Topics

## Geocoding issues

			Amazon Quick Sight geocodes place names into latitude and longitude coordinates. It uses these coordinates to display place names on the map. Amazon Quick Sight skips any places that it can't geocode.

For this process to work properly, your data must include at least the country. Also, there can't be duplicate place names inside of a parent place name.

A few issues prevent place names from showing up on a map chart. These issues include unsupported, ambiguous, or invalid locations, as described following.

###### Topics

### Issues with unsupported areas

To map unsupported locations, include latitude and longitude coordinates in your data. Use these coordinates in the geospatial field well to make locations show on a map chart.

### Issues with ambiguous locations

Geospatial data can't contain ambiguous locations. For example, suppose that
					the data contains a city named `Springfield`, but the next
					level in the hierarchy is country. Because multiple states have a city named
						`Springfield`, it isn't possible to geocode the
					location to a specific point on a map. 

To avoid this problem, you can add enough geographical data to indicate what location should show on a map chart. For example, you can add a state level into your data and its hierarchy. Or, you might add latitude and longitude.

### Issues with invalid geospatial data

Invalid geospatial data occurs when a place name (a city, for example) is listed under an incorrect parent (a state, for example). This issue might be a simple misspelling, or data entry error.

###### Note

Amazon Quick Sight doesn't support regions (for example, West Coast or South) as geospatial data. However, you can use a region as a filter in a visual.

### Issues with the default country in geocoding

Make sure that you are using the correct default country.

The default for each hierarchy is based on the country or country field that you choose when you create the hierarchy.

To change this default, you can return to the **Create
						hierarchy** screen. Then edit or create a hierarchy, and choose a
					different country. 

If you don't create a hierarchy, your default country is based on your AWS Region. For details, see the following table.

| Region | Default country | 
|---|---|
| US West (Oregon) Region US East (Ohio) Region US East (N. Virginia) Region | US | 
| Asia Pacific (Singapore) | Singapore | 
| Asia Pacific (Sydney) | Australia | 
| Europe (Ireland) Region | Ireland | 

## Issues with latitude and longitude

			Amazon Quick Sight uses latitude and longitude coordinates in the background to find place names on a map. However, you can also use coordinates to create a map without using place names. This approach also works with unsupported place names.

Latitude and longitude values must be numeric. For example, the map point
				indicated by `28.5383355 -81.3792365` is compatible with
				Amazon Quick Sight. But `28° 32' 18.0096'' N 81° 22' 45.2424'' W` is not. 

###### Topics

### Valid ranges for latitude and longitude coordinates

Amazon Quick Sight supports latitude and longitude coordinates within specific ranges.

| Coordinate | Valid range | 
|---|---|
| Latitude | Between -90 and 90 | 
| Longitude | Between -180 to 180 | 

Amazon Quick Sight skips any data outside these ranges. Out-of-range points can't be mapped on a map chart.

### Using coordinates in degrees, minutes, and seconds (DMS) format

You can use a calculated field with a formula to create a numeric latitude and longitude out of character strings. Use this section to find different ways that you can create calculated fields in Amazon Quick Sight, to parse GPS latitude and longitude into numeric latitude and longitude.

The following sample converts latitude and longitude to numeric format from
					separate fields. For example, suppose that you parse ```
51° 30'
						26.4636'' N 0° 7' 39.9288'' W
```
 using space as a delimiter. In
					this case, you can use something like the following sample to convert the
					resulting fields to numeric latitude and longitude. 

In this example, the seconds are followed by two single quotation marks. If
					your data has a double quotation mark instead, then you can use
						`strlen(LatSec)-1)` instead of
					`strlen(LatSec)-2)`.

`/*Latitude*/ ifelse( LatDir = "N", parseInt(split(LatDeg, "°", 1)) + (parseDecimal(split(LatMin, "'", 1) ) /60) + (parseDecimal((substring(LatSec, 1, strlen(LatSec)-2) ) ) /3600), (parseInt(split(LatDeg, "°", 1)) + (parseDecimal(split(LatMin, "'", 1) ) /60) + (parseDecimal((substring(LatSec, 1, strlen(LatSec)-2) ) ) /3600)) * -1 ) /*Longitude*/ ifelse( LongDir = "E", parseInt(split(LongDeg, "°", 1)) + (parseDecimal(split(LongMin, "'", 1) ) /60) + (parseDecimal((substring(LongSec, 1, strlen(LongSec)-2) ) ) /3600), (parseInt(split(LongDeg, "°", 1)) + (parseDecimal(split(LongMin, "'", 1) ) /60) + (parseDecimal((substring(LongSec, 1, strlen(LongSec)-2) ) ) /3600)) * -1 )`

If your data doesn't include the symbols for degree, minute and second, the formula looks like the following.

`/*Latitude*/ ifelse( LatDir = "N", (LatDeg + (LatMin / 60) + (LatSec / 3600)), (LatDeg + (LatMin / 60) + (LatSec / 3600)) * -1 ) /*Longitude*/ ifelse( LongDir = "E", (LongDeg + (LongMin / 60) + (LongSec / 3600)), (LongDeg + (LongMin / 60) + (LongSec / 3600)) * -1 )`

The following sample converts `53°21'N 06°15'W` to
					numeric format. However, without the seconds, this location doesn't map as
					accurately.

`/*Latitude*/ ifelse( right(Latitude, 1) = "N", (parseInt(split(Latitude, '°', 1)) + parseDecimal(substring(Latitude, (locate(Latitude, '°',3)+1), 2) ) / 60) , (parseInt(split(Latitude, '°', 1)) + parseDecimal(substring(Latitude, (locate(Latitude, '°',3)+1), 2) ) / 60) * -1 ) /*Longitude*/ ifelse( right(Longitude, 1) = "E", (parseInt(split(Longitude, '°', 1)) + parseDecimal(substring(Longitude, (locate(Longitude, '°',3)+1), 2) ) / 60) , (parseInt(split(Longitude, '°', 1)) + parseDecimal(substring(Longitude, (locate(Longitude, '°',3)+1), 2) ) / 60) * -1 )`

The formats of GPS latitude and longitude can vary, so customize your formulas to match your data. For more information, see the following:

- 
						[Degrees Minutes Seconds to Decimal Degrees](https://www.latlong.net/degrees-minutes-seconds-to-decimal-degrees)on LatLong.net
- 
						[Converting Degrees/Minutes/Seconds to Decimals using SQL](https://stackoverflow.com/questions/12186110/converts-degrees-minutes-seconds-to-decimals-using-sql)on Stack Overflow
- 
						[Geographic Coordinate Conversion](https://en.wikipedia.org/wiki/Geographic_coordinate_conversion)on Wikipedia

## Supported administrative areas and postal codes by country

			The following is a list of supported administrative areas by country.

| Country name | Country code | Country | State | County | City | 
|---|---|---|---|---|---|
| Aruba | ABW | Country | Regions | Zones | |
| Afghanistan | AFG | Country | Wilayat | Wuleswali | Localities/Urban Areas | 
| Angola | AGO | Country | Provinces/Províncias | Municipios | Localities/Urban Areas | 
| Anguilla | AIA | Country | Parishes | ||
| Albania | ALB | Country | Qarqe/Qark | Communes/Bashki | Njësi/Localities/Urban Areas | 
| Andorra | AND | Country | Parishes/Parròquies | Localities/Urban Areas | |
| United Arab Emirates | ARE | Country | Emirates | Municipalities | Cities/Localities/Urban Areas | 
| Argentina | ARG | Country | Provinces/Provincias | Departamentos/Departments | Comunas/Barrios | 
| Armenia | ARM | Country | Provinces/Marzpet | Localities/Urban Areas | |
| American Samoa | ASM | Country | Districts | Counties | Villages | 
| Antarctica | ATA | Country | |||
| French Southern Territories | ATF | Country | Districts | ||
| Antigua and Barbuda | ATG | Country | Parishes | Localities/Urban Areas | |
| Australia | AUS | Country | States | Local Government Areas | Suburbs/Urban Centers | 
| Austria | AUT | Country | States/Bundesländer | Districts/Bezirke | Municipalities/Gemeinden/Urban Areas/Stadtteil | 
| Azerbaijan | AZE | Country | Regions/Iqtisadi Rayonlar | Districts/Rayonlar | Localities/Urban Areas | 
| Burundi | BDI | Country | Provinces | Communes | Localities/Urban Areas | 
| Belgium | BEL | Country | Regions/Gewest | Provinces/Provincie | Districts/Arrondissements/Municipalities/Communes | 
| Benin | BEN | Country | Departments | Communes | Localities/Urban Areas | 
| Bonaire, Sint Eustasius, and Saba | BES | Country | Municipalities | Localities/Urban Areas | |
| Burkina Faso | BFA | Country | Regions | Provinces | Communes/Localities/Urban Areas | 
| Bangladesh | BGD | Country | Divisions/Bibhag | Districts/Zila | Subdistricts/Upzila/Localities/Urban Areas | 
| Bulgaria | BGR | Country | Oblasts | Obshtina | Localities/Urban Areas | 
| Bahrain | BHR | Country | Governorates | Constituencies | Localities | 
| Bahamas | BHS | Country | Island Groups | Districts | Towns | 
| Bosnia and Herzegovina | BIH | Country | Federation/Republika | Kanton | Opština/Localities/Urban Areas | 
| Saint Barthélemy | BLM | Country | Localities/Urban Areas | ||
| Belarus | BLR | Country | Voblasts | Rayon | Selsoviet/Localities/Urban Areas | 
| Belize | BLZ | Country | Districts | Constituencies | Localities/Urban Areas | 
| Bermuda | BMU | Country | Parishes | Localities/Urban Areas | |
| Bolivia | BOL | Country | Provinces/Provincias | Departamentos/Departments | Municipalities/Municipios/Localities/Urban Areas | 
| Brazil | BRA | Country | Provinces/States/Unidades | Municipalities/Municipios | Localities/Urban Areas | 
| Barbados | BRB | Country | Parishes | Localities/Urban Areas | |
| Brunei | BRN | Country | Districts/Dawaïr | Subdistricts/Mukim | Villages/Kampung/Localities/Urban Areas | 
| Bhutan | BTN | Country | Districts/Dzongkhag | Localities/Urban Areas | |
| Bouvet Island | BVT | Country | |||
| Botswana | BWA | Country | Districts | Subdistricts | Localities/Urban Areas | 
| Central African Republic | CAF | Country | Regions | Prefectures | Sub Prefectures/Communes | 
| Canada | CAN | Country | Provinces/Territories | Census Divisions | Census Subdivisions/Localities/Urban Areas | 
| Switzerland | CHE | Country | Cantons/Kanton/Cantone/Chantun | District/Bezirk/Distretto/Circul | "Commune/Gemeinde/Comune/Cumün/Localities/Urban Areas" | 
| Chile | CHL | Country | Regions/Regiones | Province/Provincias | Communes/Comunas/Localities/Urban Areas | 
| China, People's Republic of | CHN | Country | Provinces | Prefectures | Cities/Counties | 
| Cote d'Ivoire | CIV | Country | Districts | Regions | Departments/Sub Prefectures | 
| Cameroon | CMR | Country | Provinces/Regions | Departments | Arrondissements/Cities | 
| Congo, Democratic Republic of | COD | Country | Provinces | Districts | Localities/Urban Areas | 
| Congo, Republic of | COG | Country | Departments | Communes/Arrondissements | |
| Cook Islands | COK | Country | Island Councils | ||
| Colombia | COL | Country | Departmentos | Municipios | Localities/Urban Areas | 
| Comoros | COM | Country | Autonomous Islands/îles Autonomes | Villes/Villages | |
| Clipperton Island | CPT | Country | |||
| Cape Verde | CPV | Country | Ilhas | Concelhos | Localities/Urban Areas | 
| Costa Rica | CRI | Country | Provincias | Cantons | Distritos/Localities/Urban Areas | 
| Cuba | CUB | Country | Provincias | Municipios | Localities/Urban Areas | 
| Curaçoa | CUW | Country | Localities/Urban Areas | ||
| Cayman Islands | CYM | Country | Districts | ||
| Cyprus | CYP | Country | Districts/Eparchies | Municipalities/Dimos | Localities/Urban Areas/Sinikia | 
| Czech Republic | CZE | Country | Regions/Kraj | Municipalities/Orp | Obec/Mesto | 
| Germany | DEU | Country | Bundesland/States | Kreis/Districts | Gemeinde/Municipalities/Stadtteil/Localities/Urban Areas | 
| Djibouti | DJI | Country | Regions | Localities/Urban Areas | |
| Dominica | DMA | Country | Parishes | Localities/Urban Areas | |
| Denmark | DNK | Country | Regions | Provinces | Municipalities/Localities/Urban Areas | 
| Dominican Republic | DOM | Country | Regions/Regiones | Provinces/Provincias | Municipalities/Municipios/Localities/Urban Areas | 
| Algeria | DZA | Country | Provinces/Wilayas | Districts | Municipalities/Baladiyas/Localities/Urban Areas | 
| Ecuador | ECU | Country | Provinces | Cantons | Parishes/Localities/Urban Areas | 
| Egypt | EGY | Country | Governorates/Muhafazat | Municipal Divisions/Markaz | Towns/Cities/Sub Municipal Divisions | 
| Eritrea | ERI | Country | Regions/Zoba | Districts/Subzobas | Localities/Urban Areas | 
| Spain | ESP | Country | Autonomous Communities/Comunidados Autonomas | Provincias | Municipios/Localities/Urban Areas | 
| Estonia | EST | Country | Maakond | Omavalitsus/Linn/Vald | Küla/Localities/Urban Areas | 
| Ethiopia | ETH | Country | Regions/Kililoch | Zones/Zonouch | Localities/Urban Areas | 
| Finland | FIN | Country | Regions/Maakunta | Sub-Regions/Seutukunta | Municipalities/Kunta/Localities/Urban Areas | 
| Fiji | FJI | Country | Divisions | Provinces | Districts/Villages | 
| Falkland Islands | FLK | Country | |||
| France | FRA | Country | Regions | Départements | Arrondissements/Cantons | 
| Faroe Islands | FRO | Country | Regions/Syslur | Municipalities/Kommunur | Localities/Urban Areas | 
| Federated States of Micronesia | FSM | Country | States | ||
| Gabon | GAB | Country | Provinces | Departments | Localities/Urban Areas | 
| United Kingdom | GBR | Country | Nations | Counties | Districts/Localities/Urban Areas | 
| Georgia | GEO | Country | Regions/Mkhare | Municipalities/Munitsipaliteti | Localities/Urban Areas | 
| Ghana | GHA | Country | Regions | Districts | Localities/Urban Areas | 
| Gibraltar | GIB | Country | Localities/Urban Areas | ||
| Guinea | GIN | Country | Regions | Prefectures | Sub Prefectures/Localities/Urban Areas | 
| Guadeloupe | GLP | Country | Arrondissements | Communes | Localities/Urban Areas | 
| Gambia | GMB | Country | Regions | Districts | Localities/Urban Areas | 
| Guinea Bissau | GNB | Country | Regions | Sectors | Localities/Urban Areas | 
| Equatorial Guinea | GNQ | Country | Regions | Provincias | Distritos/Localities/Urban Areas | 
| Greece | GRC | Country | Regions/Periphenies | Regional Units Peri Enotities | Municipalities/Domoi/Localities/Urban Areas | 
| Grenada | GRD | Country | States | Parishes/Dependencies | Localities/Urban Areas | 
| Greenland | GRL | Country | Municipalities/Kommunia | ||
| Guatemala | GTM | Country | Departments/Departamentos | Municipalities/Municipios | Localities/Urban Areas | 
| French Guiana | GUF | Country | Arrondissements | Communes | Localities/Urban Areas | 
| Guam | Country = USA | States | Districts | ||
| Guyana | GUY | Country | Regions | Neighborhood Councils | Localities/Urban Areas | 
| Hong Kong | HKG | Country | Districts | Subdistricts | Localities/Urban Areas | 
| Heard and McDonald Islands | HMD | Country | |||
| Honduras | HND | Country | Departments/Departamentos | Municipalities/Municipios | Localities/Urban Areas | 
| Croatia | HRV | Country | Counties | Municipalities | Localities/Urban Areas | 
| Haiti | HTI | Country | Departments/Départements | Districts/Arrondissements | Communes/Localities/Urban Areas | 
| Hungary | HUN | Country | Regiok | Megyék | Járások/Városok | 
| Indonesia | IDN | Country | Provinces/Provinsi | Regency/Kabupaten | Districts/Kecamatan/Localities/Urban Areas | 
| India | IND | Country | States/Territories | Districts | Subdistricts/Towns/Localities/Urban Areas | 
| British Indian Ocean Territory | IOT | Country | |||
| Ireland | IRL | Country | Regions | Counties | Electoral Divisions/Localities/Urban Areas | 
| Iran | IRN | Country | Provinces/Ostanha | Counties/Shahrestan | Localities/Dehestân | 
| Iraq | IRQ | Country | Governorates/Muhafazat | Districts/Qadaa/Kaza | Urban Areas/Localities | 
| Iceland | ISL | Country | Regions/Landsvaedi | Municipalities/Sveitarfelog | Localities/Urban Areas | 
| Israel | ISR | Country | Districts | Cities/Local Councils | Localities/Urban Areas | 
| Italy | ITA | Country | Regiones | Provincias | Communes/Localities/Urban Areas | 
| Jamaica | JAM | Country | Counties | Parishes | Constituencies/Localities/Urban Areas | 
| Jordan | JOR | Country | Governorates | Districts | Subdistricts/Cities | 
| Japan | JPN | Country | Prefectures | Cities/Districts/Municipalities | |
| Kazakhstan | KAZ | Country | Regions/Oblystar | Districts/Audandar | Towns/Kent/Localities/Urban Areas | 
| Kenya | KEN | Country | Counties | Constituencies | Localities/Urban Areas/Suburbs | 
| Kyrgyzstan | KGZ | Country | Regions/Oblasttar | Districts/Raions | Localities/Urban Areas | 
| Cambodia | KHM | Country | Provinces/Khaet | Districts/Srŏk | Communes/Khum/Localities/Urban Areas | 
| Kiribati | KIR | Country | Districts | Island Councils | |
| Saint Kitts and Nevis | KNA | Country | Parishes | States | Localities/Urban Areas | 
| South Korea | KOR | Country | Provinces/Do | Districts/Si/Gun | Localities/Urban Areas | 
| Kuwait | KWT | Country | Governorates/Muhafazah | Areas/Mintaqah | Cities/Communities | 
| Laos | LAO | Country | Provinces/Khoueng | Districts/Muang | Localities/Urban Areas | 
| Lebanon | LBN | Country | Governorates/Muhafazat | Districts/Qadaa | Municipalities/Localities/Urban Areas | 
| Liberia | LBR | Country | Counties | Districts | Clans/Localities/Urban Areas | 
| Libya | LBY | Country | Districts/Shabiya | Cities/Localities/Urban Areas | |
| Saint Lucia | LCA | Country | Districts/Quarters | Localities/Urban Areas | |
| Liechtenstein | LIE | Country | Districts/Bezirk | Municipalities/Gemeinden | Localities/Urban Areas | 
| Sri Lanka | LKA | Country | Provinces | Districts | Divisional Secretariats/Localities/Urban Areas | 
| Lesotho | LSO | Country | Districts | Constituencies | Community Councils/Localities | 
| Lithuania | LTU | Country | Apskritis | Savivaldybé | Seniūnija | 
| Luxembourg | LUX | Country | Cantons/Kantounen/Kantone | Communes/Gemengen/Gemeinden | Localities/Ortschaft/Uertschaft/Cities | 
| Latvia | LVA | Country | Regions | Municipalities/Novadi | Pilsētas/Pagasti/Localities/Urban Areas | 
| Macao | MAC | Country | Parishes | Districts | |
| Saint Martin | MAF | Country | Localities/Urban Areas | ||
| Morocco | MAR | Country | Regions | Provinces/Prefectures | Communes/Localities/Urban Areas | 
| Monaco | MCO | Country | Communes | Wards/Quartiers | |
| Moldova | MDA | Country | Raion | Comuna | Localities/Urban Areas | 
| Madagascar | MDG | Country | Regions/Faritra | Districts | Communes/Localities/Urban Areas | 
| Maldives | MDV | Country | Atolls/Cities | Islands | |
| Mexico | MEX | Country | Estados | Municipios/Delegaciones | Colonias/Localities/Urban Areas | 
| Marshall Islands | MHL | Country | Municipalities | ||
| Macedonia | MKD | Country | Statistical Regions | Opstina | Localities/Urban Areas | 
| Mali | MLI | Country | Regions | Communes | Localities/Urban Areas | 
| Malta | MLT | Country | Districts | Local Councils/Kunsilli Lokali | Localities/Urban Areas | 
| Myanmar | MMR | Country | States/Regions/Union Territories | Districts | Townships/Localities/Urban Areas | 
| Montenegro | MNE | Country | Opštine/Municipalities | Localities/Urban Areas | |
| Mongolia | MNG | Country | Regions | Provinces/Aimags | Districts/Sums/Localities/Urban Areas | 
| Northern Mariana Islands | MNP | Country | Municipalities | ||
| Mozambique | MOZ | Country | Provinces | Districts/Distritos | Localities/Urban Areas | 
| Mauritania | MRT | Country | Regions | Départements | Localities/Urban Areas | 
| Montserrat | MSR | Country | Parishes | Regions | Localities/Urban Areas | 
| Martinique | MTQ | Country | Arrondissements | Communes | Localities/Urban Areas | 
| Mauritius | MUS | Country | Islands | Districts | Wards/Localities/Urban Areas | 
| Malawi | MWI | Country | Regions | Districts | Localities/Urban Areas | 
| Malaysia | MYS | Country | States/Negeri | Districts/Daïra/Daerah | Subdistricts/Mukim/Localities/Urban Area/Bahagian Kecil | 
| Mayotte | MYT | Country | Communes | Villages | |
| Namibia | NAM | Country | Provinces | Constituencies | Suburbs/Localities | 
| New Caledonia | NCL | Country | Provinces | Communes | |
| Niger | NER | Country | Regions | Departments | Localities/Urban Areas | 
| Nigeria | NGA | Country | States | Local Government Areas | Towns/Cities | 
| Nicaragua | NIC | Country | Departments/Departamentos | Municipalities/Municipios | Localities/Urban Areas | 
| Niue | NIU | Country | Villages | Towns | |
| Netherlands | NLD | Country | Counties/Fylker | Districts/Okonomisk | Municipalities, Kommuner, Localities, or Urban Areas | 
| Norway | NOR | Country | Counties/Fylker | Districts/Okonomisk | Municipalities, Kommuner, Localities, or Urban Areas | 
| Nepal | NPL | Country | Provinces/Pradeshaharu | Districts/Jilla | Municipalities/Localities/Urban Areas | 
| Nauru | NRU | Country | Districts | ||
| New Zealand | NZL | Country | Regions | Territorial Authorities | Statistical Areas/Localities/Urban Areas | 
| Oman | OMN | Country | Governorates/Muhafazah | Provinces/Wilayat | Cities/Urban Areas/Communities | 
| Pakistan | PAK | Country | Provinces | Districts | Localities/Tehsils | 
| Panama | PAN | Country | Provinces/Provincias | Districts/Distrito | Corregimientos/Localities/Urban Areas | 
| Pitcairn Islands | PCN | Country | Islands | ||
| Peru | PER | Country | Regions | Districts | Distritos/Localities/Urban Areas | 
| Philippines | PHL | Country | Regions/Rehiyon | Provinces/Lalawigan | Municipalities/Munisipiyos/Cities/Lungsod | 
| Palau | PLW | Country | States | ||
| Papua New Guinea | PNG | Country | Regions | Provinces | Districts/Localities/Urban Areas | 
| Poland | POL | Country | Provinces/Voivodeships | Counties/Powiats | Communes/Gminas/Towns/Dzielnicas | 
| North Korea | PRK | Country | Provinces | Localities/Urban Areas | |
| Portugal | PRT | Country | Districts/Distritos | Municipalities/Concelhos | Civil Parish/Freguesias/Localities/Urban Areas | 
| Paraguay | PRY | Country | Departments | Distritos | Localities/Urban Areas | 
| Palestine | PSE | Country | Territories | Governorates/Muhafazat | Localities/Urban Areas | 
| French Polynesia | PYF | Country | Subdivisions/Iles | Communes | |
| Qatar | QAT | Country | Municipalities/Baladiyat | Zones | Localities/Urban Areas | 
| Réunion | REU | Country | Arrondissements | Communes | Localities/Urban Areas | 
| Romania | ROU | Country | Regions/Judete | Communes | Towns/Oraș | 
| Russia | RUS | Country | Federal District/Federal'nyy Okrug | Oblast' | Rayon/Raion/Urban Area/Gorod | 
| Rwanda | RWA | Country | Provinces | Districts | Sectors/Secteurs/Localities/Urban Areas | 
| Saudi Arabia | SAU | Country | Regions/Manatiq | Governorates/Muhafazat | Municipalities/Amanah | 
| Sudan | SDN | Country | States/Wilaya'at | Localities/Urban Areas | |
| Senegal | SEN | Country | Regions | Departments | Arrondissements/Localities/Urban Areas | 
| Singapore | SGP | Country | Districts | Constituencies | Wards | 
| Saint Helena | SHN | Country | Islands | Districts | Localities/Urban Areas | 
| Solomon Islands | SLB | Country | Provinces | Constituencies | Wards | 
| Sierra Leone | SLE | Country | Provinces | Districts | Chiefdoms/Localities/Urban Areas | 
| El Salvador | SLV | Country | Departments/Departamentos | Municipalities/Municipios | Localities/Urban Areas | 
| San Marino | SMR | Country | Municipalities/Castelli | Localities/Urban Areas | |
| Somalia | SOM | Country | Regions/Gobolada | Localities/Urban Areas | |
| Saint Pierre and Miquelon | SPM | Country | Communes | ||
| Serbia | SRB | Country | Autonomna Pokrajina/Regions | Okrug/Districts | Opstina/Municipalities/Localities/Urban Areas | 
| South Sudan | SSD | Country | States/Wilayat | Counties | Localities/Urban Areas | 
| São Tomé and Príncipe | STP | Country | Provinces | Districts | Localities/Urban Areas | 
| Suriname | SUR | Country | Districts/Distrikt | Resorts | Localities/Urban Areas | 
| Slovakia | SVK | Country | Regions/Kraje | Districts/Okresy | Municipalities/Obec/Mestská cast | 
| Slovenia | SVN | Country | Regions/Regi | Upravne Enote | Municipalities/Obcine/Localities/Urban Areas | 
| Sweden | SWE | Country | Counties | Municipalities | Localities/Urban Areas | 
| Eswatini | SWZ | Country | Regions | Tinkhundla | Towns/Suburbs/Localities | 
| Sint Maarten | SXM | Country | Settlements | ||
| Seychelles | SYC | Country | Districts | Localities/Urban Areas | |
| Syria | SYR | Country | Governorates | Districts/Muhafazah | Cities/Localities/Urban Areas | 
| Turks and Caicos Islands | TCA | Country | Districts | Localities | |
| Chad | TCD | Country | Regions | Départements | Arrondissements/Localities/Urban Areas | 
| Togo | TGO | Country | Regions/Provinces | Prefectures | Localities/Urban Areas | 
| Thailand | THA | Country | Provinces/Changwat | Districts/Amphoe | Subdistricts/Tambon/Localities/Urban Areas | 
| Tajikistan | TJK | Country | Provinces/Regions | Districts/Raion/Rayon | Localities/Urban Areas | 
| Tokelau | TKL | Country | Atolls | ||
| Turkmenistan | TKM | Country | Provinces/Welayat | Districts/Etraplar | Towns | 
| East Timor (Timor-Leste) | TLS | Country | Municipalities | Administrative Post | Localities/Urban Areas | 
| Tonga | TON | Country | Subdivisions | ||
| Trinidad and Tobago | TTO | Country | Municipalities | Localities/Urban Areas | |
| Tunisia | TUN | Country | Governates/Wilayahs | Delegations/Mutamadiyats | Municipalities/Shaykhats/Localities/Urban Areas | 
| Turkey | TUR | Country | Provinces/Il | Districts/Ilce | Urban Areas/Belde/Subdistricts/Bucak/Neighborhoods/Mahalle | 
| Tuvalu | TUV | Country | Islands | ||
| Taiwan | TWN | Country | Provinces | Counties | Townships/Local Neighborhoods | 
| Tanzania | TZA | Country | Provinces/Mkoa | Districts/Wilaya | Localities/Urban Areas | 
| Uganda | UGA | Country | Regions | Districts | Counties/Localities/Urban Areas | 
| Ukraine | UKR | Country | Oblast/Mista/Avtonomna Respublika | Raions | Settlement Councils/Rural Councils/Localities/Urban Areas | 
| United States Minor Outlying Islands | UMI | Country | Islands/Atolls | ||
| Uruguay | URY | Country | Departments/Departamentos | Municipios/Municipalities/Secciones | Segmentos/Localities/Urban Areas | 
| United States of America | USA | Country | States/Territories | Counties | MCD/CCD/Post Localities/Municipalities | 
| Uzbekistan | UZB | Country | Regions/Viloyatlar | Districts/Tumanlar | Localities/Urban Areas | 
| Vatican City | VAT | Country | Localities/Urban Areas | ||
| Saint Vincent and the Grenadines | VCT | Country | Parishes | Divisions | Localities/Urban Areas | 
| Venezuela | VEN | Country | States/Estados | Municipalities/Municipios | Localities/Urban Areas/Parish/Parroquias | 
| British Virgin Islands | VGB | Country | Districts | ||
| Vietnam | VNM | Country | Provinces/Cities | Districts | Wards/Localities/Urban Areas | 
| Vanuatu | VUT | Country | Provinces | ||
| Wallis and Futuna Islands | WLF | Country | Districts/Rayaumes | ||
| Samoa | WSM | Country | Districts/Itūmālō | Towns | Localities/Urban Areas | 
| Kosovo | XKS | Country | Districts | Municipalities | Localities/Urban Areas | 
| Yemen | YEM | Country | Governorates/Muhafazat | Districts/Muderiah | Localities/Urban Areas | 
| South Africa | ZAF | Country | Provinces | Districts | Municipalities/Wards | 
| Zambia | ZMB | Country | Provinces | Districts | Suburbs/Localities | 
| Zimbabwe | ZWE | Country | Provinces | Districts/Muderiah | Localities/Urban Areas | 

The following is a list of the supported postal code formats by country, including the number of digits and an example postal code.

###### Note

PO BOX zipcodes are not supported postal code formats. Union territory zip codes that are used in India are also not supported.

| Country | Postal format | Example | 
|---|---|---|
| Afghanistan | 4 digit | 1001 | 
| Albania | 4 digit | 1001 | 
| Algeria | 5 digit | 01000 | 
| American Samoa | 5 digit | 96799 | 
| Andorra | 5 digit | AD100 | 
| Anguilla | 6 digit | AI-2640 | 
| Argentina | 5 digit | A4126 | 
| Armenia | 2 digit | 00 | 
| Australia | 4 digit | 0800 | 
| Austria | 4 digit | 1010 | 
| Azerbaijan | 2 digit | 01 | 
| Brunei Darussalam | 6 digit | BA1111 | 
| Bahrain | 4 digit | 0101 | 
| Bangladesh | 2 digit | 10 | 
| Belarus | 6 digit | 202115 | 
| Belgium | 4 digit | 1000 | 
| Bermuda | 4 digit | CR 01 | 
| Bhutan | 2 digit | 11 | 
| Bosnia and Herzegovina | 5 digit | 70101 | 
| Brazil | 5 digit | 01001 | 
| British Indian Ocean Territory | Alphanumeric ‐ 5 digit | BBND 1 | 
| British Virgin Islands | 4 digit | 1110 | 
| Bulgaria | 4 digit | 1000 | 
| Cabo Verde | 4 digit | 1101 | 
| Cambodia | 2 digit | 01 | 
| Canada | 3 digit | A0A | 
| Cayman Islands | Alphanumeric - 7 digit | KY1-1000 | 
| Chile | 3 digit | 100 | 
| China | 4 digit | 0100 | 
| Colombia | 4 digit | 0500 | 
| Costa Rica | 5 digit | 10101 | 
| Croatia | 5 digit | 10000 | 
| Cuba | 1 digit | 1 | 
| Cyprus | 4 digit | 1010 | 
| Czechia | 5 digit | 100 00 | 
| Democratic Republic of the Congo | 4 digit | 1001 | 
| Denmark | 4 digit | 1050 | 
| Dominican Republic | 5 digit | 10101 | 
| Ecuador | 6 digit | 010101 | 
| Egypt | 2 digit | 11 | 
| El Salvador | 4 digit | 1101 | 
| Estonia | 5 digit | 10001 | 
| Falkland Islands | Alphanumeric - 5 digit | FIQQ 1 | 
| Faroe Islands | 3 digit | 100 | 
| Finland | 5 digit | 00100 | 
| France | 5 digit | 01000 | 
| French Guiana | 5 digit | 97300 | 
| French Polynesia | 5 digit | 98701 | 
| Georgia | 2 digit | 01 | 
| Germany | 5 digit | 01067 | 
| Ghana | 2 digit | A2 | 
| Gibraltar | Alphanumeric - 5 digit | GX11 1 | 
| Greece | 5 digit | 104 31 | 
| Greenland | 4 digit | 3900 | 
| Guadeloupe | 5 digit | 97100 | 
| Guam | 5 digit | 96910 | 
| Guatemala | 5 digit | 01001 | 
| Guernsey | Alphanumeric - 4 digit, 5 digit | GY1 1, GY10 1 | 
| Guinea-Bissau | 4 digit | 1000 | 
| Haiti | 4 digit | 1110 | 
| Holy See | 5 digit | 00120 | 
| Honduras | 2 digit | 11 | 
| Hungary | 4 digit | 1007 | 
| Iceland | 3 digit | 101 | 
| India | 6 digit | 110001 | 
| Indonesia | 5 digit | 10110 | 
| Iran | 2 digit | 11 | 
| Iraq | 2 digit | 10 | 
| Ireland | 3 digit | A41 | 
| Isle of Man | Alphanumeric - 4 digit | IM1 1 | 
| Israel | 5 digit | 10292 | 
| Italy | 5 digit | 00010 | 
| Japan | 7 digit | 001-0010 | 
| Jersey | Alphanumeric - 4 digit | JE2 3 | 
| Jordan | 5 digit | 11100 | 
| Kazakhstan | 4 digit | 0100 | 
| Kenya | 1 digit | 0 | 
| Kiribati | 6 digit | KI0101 | 
| Kosovo | 5 digit | 10000 | 
| Kuwait | 2 digit | 00 | 
| Kyrgyzstan | 4 digit | 7200 | 
| Laos | 2 digit | 01 | 
| Latvia | 4 digit | 1001 | 
| Lesotho | 1 digit | 1 | 
| Liberia | 2 digit | 10 | 
| Liechtenstein | 4 digit | 9485 | 
| Lithuania | 5 digit | 00100 | 
| Luxembourg | 4 digit | 1110 | 
| Macedonia | 4 digit | 1000 | 
| Madagascar | 3 digit | 101 | 
| Malawi | 3 digit | 101 | 
| Malaysia | 5 digit | 01000 | 
| Maldives | 2 digit | 00 | 
| Malta | 3 digit | ATD | 
| Marshall Islands | 3 digit | 969 | 
| Martinique | 5 digit | 97200 | 
| Mauritius | 3 digit | 111 | 
| Mayotte | 5 digit | 97600 | 
| Mexico | 5 digit | 01000 | 
| Micronesia | 5 digit | 96941 | 
| Moldova | 4 digit | 2001 | 
| Monaco | 5 digit | 98000 | 
| Mongolia | 4 digit | 1200 | 
| Montenegro | 5 digit | 81000 | 
| Montserrat | 4 digit | 1120 | 
| Morocco | 5 digit | 10000 | 
| Mozambique | 4 digit | 1100 | 
| Myanmar | 2 digit | 01 | 
| Namibia | 3 digit | 100 | 
| Nepal | 3 digit | 101 | 
| Netherlands | 4 digit | 1011 | 
| New Caledonia | 5 digit | 98800 | 
| New Zealand | 4 digit | 0110 | 
| Nicaragua | 3 digit | 110 | 
| Niger | 4 digit | 1000 | 
| Nigeria | 4 digit | 1002 | 
| Niue | 4 digit | 9974 | 
| Norfolk Island | 4 digit | 2899 | 
| Northern Mariana Islands | 5 digit | 96950 | 
| Norway | 4 digit | 0010 | 
| Oman | 1 digit | 1 | 
| Pakistan | 2 digit | 10 | 
| Palau | 5 digit | 96939 | 
| Palestine | 4 digit | P104 | 
| Papua New Guinea | 3 digit | 111 | 
| Paraguay | 6 digit | 001001 | 
| Peru | 5 digit | 01000 | 
| Philippines | 4 digit | 1000 | 
| Pitcairn | Alphanumeric - 5 digit | PCRN 1 | 
| Poland | 5 digit | 00-002 | 
| Portugal | 4 digit | 1000 | 
| Puerto Rico | 5 digit | 00601 | 
| Romania | 6 digit | 010011 | 
| Russia | 6 digit | 101000 | 
| Réunion | 5 digit | 97400 | 
| Saint Barthélemy | 5 digit | 97133 | 
| Saint Helena, Ascension and Tristan da Cunha | Alphanumeric - 5 digit | ASCN 1 | 
| Saint Lucia | 7 digit | LC01 101 | 
| Saint Martin | 5 digit | 97150 | 
| Saint Pierre and Miquelon | 5 digit | 97500 | 
| Saint Vincent and the Grenadines | 4 digit | VC01 | 
| Samoa | 2 digit | 11 | 
| San Marino | 5 digit | 47890 | 
| Saudi Arabia | 2 digit | 12 | 
| Senegal | 5 digit | 10000 | 
| Serbia | 5 digit | 11000 | 
| Singapore | 6 digit | 018906 | 
| Slovakia | 5 digit | 010 01 | 
| Slovenia | 4 digit | 1000 | 
| South Africa | 4 digit | 0001 | 
| South Georgia and the South Sandwich Islands | Alphanumeric - 5 digit | SIQQ 1 | 
| South Korea | 5 digit | 01000 | 
| Spain | 5 digit | 01001 | 
| Sri Lanka | 2 digit | 00 | 
| Sudan | 2 digit | 11 | 
| Svalbard and Jan Mayen | 4 digit | 8099 | 
| Swaziland | 1 digit | H | 
| Sweden | 5 digit | 111 15 | 
| Switzerland | 4 digit | 1000 | 
| Taiwan | 3 digit | 100 | 
| Tajikistan | 4 digit | 7340 | 
| Tanzania, United Republic of | 3 digit | 111 | 
| Thailand | 5 digit | 10100 | 
| Timor-Leste | 4 digit | TL10 | 
| Trinidad and Tobago | 2 digit | 10 | 
| Tunisia | 4 digit | 1000 | 
| Turkey | 5 digit | 01010 | 
| Turkmenistan | 3 digit | 744 | 
| Turks and Caicos Islands | Alphanumeric - 5 digit | TKCA 1 | 
| U.S. Virgin Islands | 5 digit | 00802 | 
| Ukraine | 3 digit, 5 digit | 070, 01001 | 
| United Kingdom | Alphanumeric - 2 to 5 digits | B1, AL1, AB10, AB10 1 | 
| United States | 5 digit | 00001 | 
| Uruguay | 5 digit | 11000 | 
| Uzbekistan | 4 digit | 1000 | 
| Venezuela | 4 digit | 0000 | 
| Vietnam | 5 digit | 01106 | 
| Wallis and Futuna | 5 digit | 98600 | 
| Zambia | 5 digit | 10100 |