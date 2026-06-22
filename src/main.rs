use reqwest::Error;
use serde::Deserialize;

#[derive(Deserialize)]
struct WeatherResponse {
    current_weather: CurrentWeather,
}

#[derive(Deserialize)]
struct CurrentWeather {
    temperature: f64,
    windspeed: f64,
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    let cities = [
        ("Tokyo", 35.6762, 139.6503),
        ("Jakarta", -6.2088, 106.8456),
        ("Bangkok", 13.7563, 100.5018),
        ("Paris", 48.8566, 2.3522),
    ];

    for (name, lat, lon) in cities {
        let url = format!(
            "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true",
            lat, lon
        );

        let response: WeatherResponse = reqwest::get(&url).await?.json().await?;

        println!(
            "{}: {:.1}°C, Wind: {:.1} km/h",
            name,
            response.current_weather.temperature,
            response.current_weather.windspeed
        );
    }

    Ok(())
}
