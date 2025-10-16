

Example of Response body

```
{
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    {
      "@version": "1.1",
      "wx": "https://api.weather.gov/ontology#",
      "@vocab": "https://api.weather.gov/ontology#"
    }
  ],
  "type": "FeatureCollection",
  "features": [
    {
      "id": "https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.40e43782e669d338055cc618ebdbb9a17df36b2b.001.1",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "@id": "https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.40e43782e669d338055cc618ebdbb9a17df36b2b.001.1",
        "@type": "wx:Alert",
        "id": "urn:oid:2.49.0.1.840.0.40e43782e669d338055cc618ebdbb9a17df36b2b.001.1",
        "areaDesc": "Skilak Lake; Interior Kenai Peninsula",
        "geocode": {
          "SAME": [
            "002122"
          ],
          "UGC": [
            "AKZ724",
            "AKZ726"
          ]
        },
        "affectedZones": [
          "https://api.weather.gov/zones/forecast/AKZ724",
          "https://api.weather.gov/zones/forecast/AKZ726"
        ],
        "references": [],
        "sent": "2025-10-14T14:53:00-08:00",
        "effective": "2025-10-14T14:53:00-08:00",
        "onset": "2025-10-14T14:53:00-08:00",
        "expires": "2025-10-15T14:00:00-08:00",
        "ends": null,
        "status": "Actual",
        "messageType": "Alert",
        "category": "Met",
        "severity": "Unknown",
        "certainty": "Possible",
        "urgency": "Future",
        "event": "Hydrologic Outlook",
        "sender": "w-nws.webmaster@noaa.gov",
        "senderName": "NWS Anchorage AK",
        "headline": "Hydrologic Outlook issued October 14 at 2:53PM AKDT by NWS Anchorage AK",
        "description": "ESFAFC\n\nBased on rising river levels on the Snow River, it is possible that\nSnow Glacier Dammed Lake is releasing. At this time, we do not\nexpect water levels to reach flood stage on the Snow River, but an\nadditional 2 to 3 feet rise of water levels is likely if a release\nis occurring.\n\nAs of 2:45PM, the current water level at Cooper Landing is 9.5 feet.\nWater levels on Kenai Lake and the Upper Kenai River have started to\nrise and would likely rise another 1 to 3 feet, cresting Friday\nbelow flood stage if a release is occurring.\n\nThere is always uncertainty with Glacier Dam Lake releases.\nResidents living around Kenai Lake should monitor conditions and\nprepare for rising water levels.\n\nThis statement will be updated daily as more information is\navailable.",
        "instruction": null,
        "response": "Monitor",
        "parameters": {
          "AWIPSidentifier": [
            "ESFAFC"
          ],
          "WMOidentifier": [
            "FGAK78 PAFC 142253"
          ],
          "NWSheadline": [
            "POSSIBLE SNOW GLACIER DAM LAKE RELEASE"
          ],
          "BLOCKCHANNEL": [
            "EAS",
            "NWEM",
            "CMAS"
          ]
        },
        "scope": "Public",
        "code": "IPAWSv1.0",
        "language": "en-US",
        "web": "http://www.weather.gov",
        "eventCode": {
          "SAME": [
            "NWS"
          ],
          "NationalWeatherService": [
            "ESF"
          ]
        }
      }
    },
    {
      "id": "https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.4fd4610b47110f6e025107a84cceabc723d78825.001.1",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "@id": "https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.4fd4610b47110f6e025107a84cceabc723d78825.001.1",
        "@type": "wx:Alert",
        "id": "urn:oid:2.49.0.1.840.0.4fd4610b47110f6e025107a84cceabc723d78825.001.1",
        "areaDesc": "Municipality of Skagway",
        "geocode": {
          "SAME": [
            "002230"
          ],
          "UGC": [
            "AKZ318"
          ]
        },
        "affectedZones": [
          "https://api.weather.gov/zones/forecast/AKZ318"
        ],
        "references": [
          {
            "@id": "https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.17caaab953c53a37de4933e81154bddb55284039.001.1",
            "identifier": "urn:oid:2.49.0.1.840.0.17caaab953c53a37de4933e81154bddb55284039.001.1",
            "sender": "w-nws.webmaster@noaa.gov",
            "sent": "2025-10-14T04:29:00-08:00"
          }
        ],
        "sent": "2025-10-14T12:57:00-08:00",
        "effective": "2025-10-14T12:57:00-08:00",
        "onset": "2025-10-14T13:00:00-08:00",
        "expires": "2025-10-14T21:00:00-08:00",
        "ends": "2025-10-14T22:00:00-08:00",
        "status": "Actual",
        "messageType": "Update",
        "category": "Met",
        "severity": "Severe",
        "certainty": "Likely",
        "urgency": "Expected",
        "event": "High Wind Warning",
        "sender": "w-nws.webmaster@noaa.gov",
        "senderName": "NWS Juneau AK",
        "headline": "High Wind Warning issued October 14 at 12:57PM AKDT until October 14 at 10:00PM AKDT by NWS Juneau AK",
        "description": "* WHAT...South winds 25 to 35 mph with gusts up to 60 mph\nexpected.\n\n* WHERE...Municipality of Skagway.\n\n* WHEN...Until 10 PM AKDT this evening.\n\n* IMPACTS...High winds will blow around unsecured objects and\nmay damage property and cause power outages. Travel will be\ndifficult.\n\n* ADDITIONAL DETAILS...The strongest wind gusts are expected\nbetween 2pm and 9pm Tuesday evening. Strong winds are still\npossible, but not as likely, earlier in the day on Tuesday as\nwell as after the warning ends. Winds are anticipated to\ndiminish during the early morning hours of Wednesday before\nthe next system moves into the area.",
        "instruction": "People are urged to secure vessels and loose objects that could\nbe blown around or damaged by the wind.\n\nReport any damage to the National Weather Service by visiting\nweather.gov/Juneau/StormReports",
        "response": "Prepare",
        "parameters": {
          "AWIPSidentifier": [
            "NPWAJK"
          ],
          "WMOidentifier": [
            "WWAK77 PAJK 142057"
          ],
          "NWSheadline": [
            "HIGH WIND WARNING NOW IN EFFECT UNTIL 10 PM AKDT THIS EVENING"
          ],
          "BLOCKCHANNEL": [
            "EAS",
            "NWEM",
            "CMAS"
          ],
          "EAS-ORG": [
            "WXR"
          ],
          "VTEC": [
            "/O.EXT.PAJK.HW.W.0009.251014T2100Z-251015T0600Z/"
          ],
          "eventEndingTime": [
            "2025-10-14T22:00:00-08:00"
          ],
          "expiredReferences": [
            "w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.b1a85ddc7bf9e1403fa5e71f1a277bd9cc61af5e.001.1,2025-10-13T20:56:00-08:00 w-nws.webmaster@noaa.gov,urn:oid:2.49.0.1.840.0.7510411937d81fb4f94769c31eef722b13d4fd66.001.1,2025-10-13T13:01:00-08:00"
          ]
        },
        "scope": "Public",
        "code": "IPAWSv1.0",
        "language": "en-US",
        "web": "http://www.weather.gov",
        "eventCode": {
          "SAME": [
            "HWW"
          ],
          "NationalWeatherService": [
            "HWW"
          ]
        }
      }
    }
  ],
  "title": "Current watches, warnings, and advisories for Alaska",
  "updated": "2025-10-15T02:00:00+00:00"
}
```