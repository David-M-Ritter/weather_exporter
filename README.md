# weather_exporter
## Export weather from open-meteo to Dynatrace as metric
This project exports the tempature from: 
Ludington, Mi; 
Lansing, Mi; 
Charlevoix, Mi; 
Paris, France; 
Syndey, Austraila 

It then exports the information to Dynatrace. You will need a Dynatrace tenant url and api-token with metrics.ingest permissions in order for this to work. 


## To run this project you must first build the container:

docker buildx build . --tag="dt_metrics"

## Then run the container with the required parameters:

docker dt_metrics run python ./metric_import.py --dt_url="https://xxxxxx.sprint.dynatracelabs.com/" --dt_api="dt0c01.xxxxx.xxxx"  
