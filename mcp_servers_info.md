# MCP Server Information Summary

## Summary Information

- **Collection Time**: 2025-12-03T16:44:43.506394
- **Connection Mode**: INDIVIDUAL
- **Total Servers**: 28
- **Successful Connections**: 28
- **Failed Connections**: 0
- **Total Tools Discovered**: 246

## Server Details

###  OpenAPI Explorer

**Description**: 

**Connection Status**: success

**Available Tools** (2 ):

#### getApiOverview

**Description**: Get an overview of an OpenAPI specification. This should be the first step when working with any API.

- openai - OpenAI is a large AI service provider providing state of the art models in various modalities.
- github - GitHub is where one hosts their code in a central location, to collaborate with others
- socialdata.tools
- podscan.fm - Search through podcast transcripts, get alerts
- x - Official Twitter/X API
- cloudflare - Cloudflare provides content delivery network services, cloud cybersecurity, DDoS mitigation, wide area network services, Domain Name Service, and ICANN-accredited domain registration services
- npm-registry
- supabase - Create hosted Postgres Databases with API
- hackernews - Readonly API for posts, comments, and profiles from news.ycombinator.com
- stripe - Create a paywall for your app or invoices
- slack - A very common app used for communication at work
- vercel - Vercel is a cloud hosting solution for full stack applications
- val-town - Host serverless APIs
- firecrawl - API for interacting with Firecrawl services to perform web scraping and crawling tasks.
- playht - The PlayHT's API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.
- serper - The worlds fastest and cheapest google search api
- replicate
- brandwatch - Watch social media about your brand
- jina-reader - Read webpages in markdown, html, or screenshot
- upstash-redis - Control a Redis database over API
- upstash-qstash - Scheduling and batching API calls
- upstash-vector - Control a Vector database over API
- digitalocean
- apisguru - Public API to find OpenAPIs on https://apis.guru
- groq - Cloud AI Provider with multiple transformer LLMs and other modalities, with very fast inference
- notion-dbs - Notion Databases API
- posthog-capture-api - Posthog is a Product analytics platform allowing companies to track and understand their users
- google-analytics4 - The Google Analytics Admin API allows for programmatic access to the Google Analytics 4 (GA4) configuration data and is only compatible with GA4 properties
- google-analytics3 - Views and manages your Google Analytics data (GA3)
- anthropic-message-api
- probo-nl
- whatsapp-business - The WhatsApp Business Platform gives medium to large businesses the ability to connect with customers at scale. You can start WhatsApp conversations with your customers in minutes, send them care notifications or purchase updates, offer personalized services, and provide support in the channel that your customers prefer.
- shopify - Shopify Admin API
- twilio-messaging
- huggingface
- doppio
- multion
- browserless - Web browsing API
- bol-com-retailer - Dutch shopping platform
- statusbrew - Social media planning API for facebook, instagram, twitter, linkedin, google my business, pinterest, youtube, and tiktok.
- swagger-validator - Validators for swagger 2.0 and 3.x specifications of OpenAPIs
- google-mail - Manage GMail
- youtube-data - The YouTube Data API v3 is an API that provides access to YouTube data, such as videos, playlists, and channels.
- google-sheets
- google-drive
- google-secret-manager
- flyio
- vapi
- klippa
- uberduck
- twilio
- saltedge - Bank integrations
- google-search-console
- aws-cloudwatch-insights
- aws-cloudfront
- aws-email
- aws-s3-control
- aws-s3
- aws-sagemaker
- aws-sagemaker-edge
- aws-sagemaker-featureStore
- bunq
- hootsuite
- robocorp
- sendgrid
- google-calendar
- google-docs

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "API identifier, can be a known ID from openapisearch.com or a URL leading to a raw OpenAPI file"
    }
  },
  "required": [
    "id"
  ]
}
```

#### getApiOperation

**Description**: Get details about a specific operation from an OpenAPI specification. Use this after getting an overview.

- openai - OpenAI is a large AI service provider providing state of the art models in various modalities.
- github - GitHub is where one hosts their code in a central location, to collaborate with others
- socialdata.tools
- podscan.fm - Search through podcast transcripts, get alerts
- x - Official Twitter/X API
- cloudflare - Cloudflare provides content delivery network services, cloud cybersecurity, DDoS mitigation, wide area network services, Domain Name Service, and ICANN-accredited domain registration services
- npm-registry
- supabase - Create hosted Postgres Databases with API
- hackernews - Readonly API for posts, comments, and profiles from news.ycombinator.com
- stripe - Create a paywall for your app or invoices
- slack - A very common app used for communication at work
- vercel - Vercel is a cloud hosting solution for full stack applications
- val-town - Host serverless APIs
- firecrawl - API for interacting with Firecrawl services to perform web scraping and crawling tasks.
- playht - The PlayHT's API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.
- serper - The worlds fastest and cheapest google search api
- replicate
- brandwatch - Watch social media about your brand
- jina-reader - Read webpages in markdown, html, or screenshot
- upstash-redis - Control a Redis database over API
- upstash-qstash - Scheduling and batching API calls
- upstash-vector - Control a Vector database over API
- digitalocean
- apisguru - Public API to find OpenAPIs on https://apis.guru
- groq - Cloud AI Provider with multiple transformer LLMs and other modalities, with very fast inference
- notion-dbs - Notion Databases API
- posthog-capture-api - Posthog is a Product analytics platform allowing companies to track and understand their users
- google-analytics4 - The Google Analytics Admin API allows for programmatic access to the Google Analytics 4 (GA4) configuration data and is only compatible with GA4 properties
- google-analytics3 - Views and manages your Google Analytics data (GA3)
- anthropic-message-api
- probo-nl
- whatsapp-business - The WhatsApp Business Platform gives medium to large businesses the ability to connect with customers at scale. You can start WhatsApp conversations with your customers in minutes, send them care notifications or purchase updates, offer personalized services, and provide support in the channel that your customers prefer.
- shopify - Shopify Admin API
- twilio-messaging
- huggingface
- doppio
- multion
- browserless - Web browsing API
- bol-com-retailer - Dutch shopping platform
- statusbrew - Social media planning API for facebook, instagram, twitter, linkedin, google my business, pinterest, youtube, and tiktok.
- swagger-validator - Validators for swagger 2.0 and 3.x specifications of OpenAPIs
- google-mail - Manage GMail
- youtube-data - The YouTube Data API v3 is an API that provides access to YouTube data, such as videos, playlists, and channels.
- google-sheets
- google-drive
- google-secret-manager
- flyio
- vapi
- klippa
- uberduck
- twilio
- saltedge - Bank integrations
- google-search-console
- aws-cloudwatch-insights
- aws-cloudfront
- aws-email
- aws-s3-control
- aws-s3
- aws-sagemaker
- aws-sagemaker-edge
- aws-sagemaker-featureStore
- bunq
- hootsuite
- robocorp
- sendgrid
- google-calendar
- google-docs

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "API identifier, can be a known ID from openapisearch.com or a URL leading to a raw OpenAPI file"
    },
    "operationIdOrRoute": {
      "type": "string",
      "description": "Operation ID or route path to retrieve"
    }
  },
  "required": [
    "id",
    "operationIdOrRoute"
  ]
}
```

---

###  Unit Converter

**Description**: 

**Connection Status**: success

**Available Tools** (16 ):

#### convert_temperature

**Description**: Convert temperature between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Temperature value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "celsius",
        "fahrenheit",
        "kelvin"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "celsius",
        "fahrenheit",
        "kelvin"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_angle

**Description**: Convert angle between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Angle value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "degrees",
        "radians",
        "arcmin",
        "arcsec",
        "turns",
        "gons"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "degrees",
        "radians",
        "arcmin",
        "arcsec",
        "turns",
        "gons"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_length

**Description**: Convert length between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Length value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "angstrom",
        "astronomical unit",
        "cable",
        "centimeter",
        "chain (surveyors)",
        "decimeter",
        "em (pica)",
        "fathom",
        "foot",
        "foot (US survey)",
        "furlong",
        "hand",
        "hectometer",
        "inch",
        "kilometer",
        "light year",
        "meter",
        "micrometer",
        "mil",
        "mile",
        "nautical mile",
        "nautical mile (UK)",
        "millimeter",
        "nanometer",
        "parsec",
        "picometer",
        "Scandinavian mile",
        "thou",
        "yard"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "angstrom",
        "astronomical unit",
        "cable",
        "centimeter",
        "chain (surveyors)",
        "decimeter",
        "em (pica)",
        "fathom",
        "foot",
        "foot (US survey)",
        "furlong",
        "hand",
        "hectometer",
        "inch",
        "kilometer",
        "light year",
        "meter",
        "micrometer",
        "mil",
        "mile",
        "nautical mile",
        "nautical mile (UK)",
        "millimeter",
        "nanometer",
        "parsec",
        "picometer",
        "Scandinavian mile",
        "thou",
        "yard"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_energy

**Description**: Convert energy between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Energy value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "joule",
        "kilojoule",
        "megajoule",
        "gigajoule",
        "terajoule",
        "petajoule",
        "exajoule",
        "watt hour",
        "kilowatt hour",
        "megawatt hour",
        "gigawatt hour",
        "terawatt hour",
        "Btu",
        "calorie",
        "kilocalorie",
        "therm",
        "foot‑pound force",
        "inch‑pound force",
        "erg",
        "electron volt"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "joule",
        "kilojoule",
        "megajoule",
        "gigajoule",
        "terajoule",
        "petajoule",
        "exajoule",
        "watt hour",
        "kilowatt hour",
        "megawatt hour",
        "gigawatt hour",
        "terawatt hour",
        "Btu",
        "calorie",
        "kilocalorie",
        "therm",
        "foot‑pound force",
        "inch‑pound force",
        "erg",
        "electron volt"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_force

**Description**: Convert force between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Force value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "dynes",
        "kilograms force",
        "kilonewtons",
        "kips",
        "meganewtons",
        "newtons",
        "pounds force",
        "tonnes force",
        "long tons force",
        "short tons force"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "dynes",
        "kilograms force",
        "kilonewtons",
        "kips",
        "meganewtons",
        "newtons",
        "pounds force",
        "tonnes force",
        "long tons force",
        "short tons force"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_pressure

**Description**: Convert pressure between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Pressure value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "pascal",
        "hectopascal",
        "kilopascal",
        "megapascal",
        "bar",
        "atmosphere",
        "centimeters of water",
        "inches of water",
        "feet of water",
        "meters of water",
        "millimeters of mercury",
        "inches of mercury",
        "kilogram force per square centimeter",
        "newtons per square centimeter",
        "newtons per square millimeter",
        "psi",
        "psf"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "pascal",
        "hectopascal",
        "kilopascal",
        "megapascal",
        "bar",
        "atmosphere",
        "centimeters of water",
        "inches of water",
        "feet of water",
        "meters of water",
        "millimeters of mercury",
        "inches of mercury",
        "kilogram force per square centimeter",
        "newtons per square centimeter",
        "newtons per square millimeter",
        "psi",
        "psf"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_power

**Description**: Convert power between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Power value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "Btu per hour",
        "foot pound‑force per second",
        "ton of refrigeration",
        "calorie per hour",
        "kilocalorie per hour",
        "horsepower",
        "horsepower (metric)",
        "kilogram‑force meter per second",
        "watt",
        "kilowatt",
        "megawatt",
        "gigawatt",
        "terawatt",
        "petawatt"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "Btu per hour",
        "foot pound‑force per second",
        "ton of refrigeration",
        "calorie per hour",
        "kilocalorie per hour",
        "horsepower",
        "horsepower (metric)",
        "kilogram‑force meter per second",
        "watt",
        "kilowatt",
        "megawatt",
        "gigawatt",
        "terawatt",
        "petawatt"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_speed

**Description**: Convert speed between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Speed value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "centimeters per minute",
        "centimeters per second",
        "feet per hour",
        "feet per minute",
        "feet per second",
        "inches per minute",
        "inches per second",
        "kilometers per hour",
        "kilometers per second",
        "knots",
        "Mach (ISA sea level)",
        "speed of sound",
        "meters per hour",
        "meters per minute",
        "meters per second",
        "miles per hour",
        "miles per minute",
        "miles per second",
        "yards per hour",
        "yards per minute",
        "yards per second",
        "speed of light"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "centimeters per minute",
        "centimeters per second",
        "feet per hour",
        "feet per minute",
        "feet per second",
        "inches per minute",
        "inches per second",
        "kilometers per hour",
        "kilometers per second",
        "knots",
        "Mach (ISA sea level)",
        "speed of sound",
        "meters per hour",
        "meters per minute",
        "meters per second",
        "miles per hour",
        "miles per minute",
        "miles per second",
        "yards per hour",
        "yards per minute",
        "yards per second",
        "speed of light"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_area

**Description**: Convert area between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Area value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "acre",
        "are",
        "hectare",
        "square centimeter",
        "square foot",
        "square inch",
        "square kilometer",
        "square meter",
        "square mile",
        "square millimeter",
        "square yard"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "acre",
        "are",
        "hectare",
        "square centimeter",
        "square foot",
        "square inch",
        "square kilometer",
        "square meter",
        "square mile",
        "square millimeter",
        "square yard"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_mass

**Description**: Convert weight between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Weight value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "carat",
        "decagram",
        "hectogram",
        "gram",
        "milligram",
        "microgram",
        "nanogram",
        "picogram",
        "femtogram",
        "grain",
        "ounce",
        "troy ounce",
        "pound",
        "stone",
        "short ton (US)",
        "long ton (UK)",
        "tonne",
        "kilotonne",
        "megatonne",
        "kilogram"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "carat",
        "decagram",
        "hectogram",
        "gram",
        "milligram",
        "microgram",
        "nanogram",
        "picogram",
        "femtogram",
        "grain",
        "ounce",
        "troy ounce",
        "pound",
        "stone",
        "short ton (US)",
        "long ton (UK)",
        "tonne",
        "kilotonne",
        "megatonne",
        "kilogram"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_volume

**Description**: Convert volume between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Volume value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "acre foot",
        "barrel (oil)",
        "bushel (UK)",
        "bushel (US)",
        "bushel",
        "centiliter",
        "cubic centimeter",
        "cubic decimeter",
        "cubic foot",
        "cubic inch",
        "cubic kilometer",
        "cubic meter",
        "cubic mile",
        "cubic millimeter",
        "cubic yard",
        "cup",
        "deciliter",
        "fluid ounce (imperial)",
        "fluid ounce (US)",
        "fluid ounce",
        "gallon (imperial)",
        "gallon (US)",
        "gallon",
        "kiloliter",
        "liter",
        "milliliter",
        "microliter",
        "nanoliter",
        "picoliter",
        "pint (imperial)",
        "pint (US)",
        "pint",
        "quart (imperial)",
        "quart (US)",
        "quart",
        "tablespoon",
        "teaspoon"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "acre foot",
        "barrel (oil)",
        "bushel (UK)",
        "bushel (US)",
        "bushel",
        "centiliter",
        "cubic centimeter",
        "cubic decimeter",
        "cubic foot",
        "cubic inch",
        "cubic kilometer",
        "cubic meter",
        "cubic mile",
        "cubic millimeter",
        "cubic yard",
        "cup",
        "deciliter",
        "fluid ounce (imperial)",
        "fluid ounce (US)",
        "fluid ounce",
        "gallon (imperial)",
        "gallon (US)",
        "gallon",
        "kiloliter",
        "liter",
        "milliliter",
        "microliter",
        "nanoliter",
        "picoliter",
        "pint (imperial)",
        "pint (US)",
        "pint",
        "quart (imperial)",
        "quart (US)",
        "quart",
        "tablespoon",
        "teaspoon"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_computer_data

**Description**: Convert computer storage between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Computer storage value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "bits",
        "bytes",
        "kilobytes",
        "megabytes",
        "gigabytes",
        "terabytes",
        "petabytes",
        "exabytes"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "bits",
        "bytes",
        "kilobytes",
        "megabytes",
        "gigabytes",
        "terabytes",
        "petabytes",
        "exabytes"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_density

**Description**: Convert density between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Density value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "grains per gallon (UK)",
        "grains per gallon (US)",
        "grains per gallon",
        "grams per cubic centimeter",
        "grams per liter",
        "kilograms per liter",
        "kilograms per cubic meter",
        "milligrams per liter",
        "ounces per gallon (UK)",
        "ounces per gallon (US)",
        "ounces per gallon",
        "pounds per cubic foot",
        "pounds per gallon (UK)",
        "pounds per gallon (US)",
        "pounds per gallon",
        "tonnes per cubic meter",
        "tons per cubic yard (UK)",
        "tons per cubic yard (US)",
        "tons per cubic yard"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "grains per gallon (UK)",
        "grains per gallon (US)",
        "grains per gallon",
        "grams per cubic centimeter",
        "grams per liter",
        "kilograms per liter",
        "kilograms per cubic meter",
        "milligrams per liter",
        "ounces per gallon (UK)",
        "ounces per gallon (US)",
        "ounces per gallon",
        "pounds per cubic foot",
        "pounds per gallon (UK)",
        "pounds per gallon (US)",
        "pounds per gallon",
        "tonnes per cubic meter",
        "tons per cubic yard (UK)",
        "tons per cubic yard (US)",
        "tons per cubic yard"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_time

**Description**: Convert time between units.

**Input Parameters**:
```json
{
  "properties": {
    "value": {
      "description": "Time value to convert",
      "type": "number"
    },
    "from_unit": {
      "description": "Source unit",
      "enum": [
        "picoseconds",
        "femtoseconds",
        "nanoseconds",
        "microseconds",
        "milliseconds",
        "seconds",
        "minutes",
        "hours",
        "days",
        "weeks",
        "fortnights",
        "months",
        "quarters",
        "synodic months",
        "years",
        "decades",
        "centuries",
        "millennia"
      ],
      "type": "string"
    },
    "to_unit": {
      "description": "Target unit",
      "enum": [
        "picoseconds",
        "femtoseconds",
        "nanoseconds",
        "microseconds",
        "milliseconds",
        "seconds",
        "minutes",
        "hours",
        "days",
        "weeks",
        "fortnights",
        "months",
        "quarters",
        "synodic months",
        "years",
        "decades",
        "centuries",
        "millennia"
      ],
      "type": "string"
    }
  },
  "required": [
    "value",
    "from_unit",
    "to_unit"
  ],
  "type": "object"
}
```

#### convert_batch

**Description**: Perform multiple unit conversions in a single batch request.

Each request in the batch should contain:
- value: The numeric value to convert
- from_unit: Source unit for conversion
- to_unit: Target unit for conversion
- conversion_type: Type of conversion (temperature, length, mass, etc.)
- request_id: Optional identifier for tracking individual requests

Returns a structured response with individual results for each conversion,
including success/failure status and either converted values or error messages.

**Input Parameters**:
```json
{
  "properties": {
    "requests": {
      "description": "List of conversion requests. Each request should contain: value (float), from_unit (str), to_unit (str), conversion_type (str), and optionally request_id (str)",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array"
    }
  },
  "required": [
    "requests"
  ],
  "type": "object"
}
```

#### list_supported_units

**Description**: List all supported units for each conversion type or for a specific type.

**Input Parameters**:
```json
{
  "properties": {
    "unit_type": {
      "anyOf": [
        {
          "enum": [
            "angle",
            "area",
            "computer_data",
            "density",
            "energy",
            "force",
            "length",
            "mass",
            "power",
            "pressure",
            "speed",
            "temperature",
            "time",
            "volume"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Specific unit type to get supported units for. If not specified, returns all supported units."
    }
  },
  "type": "object"
}
```

---

###  Wikipedia

**Description**: 

**Connection Status**: success_no_tools

**Available Tools**: None

---

###  Google Maps

**Description**: 

**Connection Status**: success

**Available Tools** (7 ):

#### search_nearby

**Description**: Search for nearby places based on location, with optional filtering by keywords, distance, rating, and operating hours

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "center": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "Address, landmark name, or coordinates (coordinate format: lat,lng)"
        },
        "isCoordinates": {
          "type": "boolean",
          "default": false,
          "description": "Whether the value is coordinates"
        }
      },
      "required": [
        "value"
      ],
      "additionalProperties": false,
      "description": "Search center point"
    },
    "keyword": {
      "type": "string",
      "description": "Search keyword (e.g., restaurant, cafe, hotel)"
    },
    "radius": {
      "type": "number",
      "default": 1000,
      "description": "Search radius in meters"
    },
    "openNow": {
      "type": "boolean",
      "default": false,
      "description": "Only show places that are currently open"
    },
    "minRating": {
      "type": "number",
      "minimum": 0,
      "maximum": 5,
      "description": "Minimum rating requirement (0-5)"
    }
  },
  "required": [
    "center"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### get_place_details

**Description**: Get detailed information about a specific place including contact details, reviews, ratings, and operating hours

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "placeId": {
      "type": "string",
      "description": "Google Maps place ID"
    }
  },
  "required": [
    "placeId"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### maps_geocode

**Description**: Convert addresses or place names to geographic coordinates (latitude and longitude)

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "address": {
      "type": "string",
      "description": "Address or place name to convert to coordinates"
    }
  },
  "required": [
    "address"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### maps_reverse_geocode

**Description**: Convert geographic coordinates (latitude and longitude) to a human-readable address

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number",
      "description": "Latitude coordinate"
    },
    "longitude": {
      "type": "number",
      "description": "Longitude coordinate"
    }
  },
  "required": [
    "latitude",
    "longitude"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### maps_distance_matrix

**Description**: Calculate travel distances and durations between multiple origins and destinations for different travel modes

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "origins": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of origin addresses or coordinates"
    },
    "destinations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of destination addresses or coordinates"
    },
    "mode": {
      "type": "string",
      "enum": [
        "driving",
        "walking",
        "bicycling",
        "transit"
      ],
      "default": "driving",
      "description": "Travel mode for calculation"
    }
  },
  "required": [
    "origins",
    "destinations"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### maps_directions

**Description**: Get detailed turn-by-turn navigation directions between two locations with route information

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "origin": {
      "type": "string",
      "description": "Starting point address or coordinates"
    },
    "destination": {
      "type": "string",
      "description": "Destination address or coordinates"
    },
    "mode": {
      "type": "string",
      "enum": [
        "driving",
        "walking",
        "bicycling",
        "transit"
      ],
      "default": "driving",
      "description": "Travel mode for directions"
    },
    "departure_time": {
      "type": "string",
      "description": "Departure time (ISO string format)"
    },
    "arrival_time": {
      "type": "string",
      "description": "Arrival time (ISO string format)"
    }
  },
  "required": [
    "origin",
    "destination"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### maps_elevation

**Description**: Get elevation data (height above sea level) for specific geographic locations

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "locations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "latitude": {
            "type": "number",
            "description": "Latitude coordinate"
          },
          "longitude": {
            "type": "number",
            "description": "Longitude coordinate"
          }
        },
        "required": [
          "latitude",
          "longitude"
        ],
        "additionalProperties": false
      },
      "description": "List of locations to get elevation data for"
    }
  },
  "required": [
    "locations"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  Bibliomantic

**Description**: 

**Connection Status**: success

**Available Tools** (4 ):

#### i_ching_divination

**Description**: 
    Enhanced I Ching divination with traditional three-coin method and changing lines.
    MAINTAINS EXACT BACKWARD COMPATIBILITY while providing richer content.
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Query"
    }
  },
  "title": "i_ching_divinationArguments",
  "type": "object"
}
```

#### bibliomantic_consultation

**Description**: 
    Enhanced bibliomantic consultation with full traditional I Ching elements.
    DRAMATICALLY IMPROVED CONTENT while maintaining exact interface compatibility.
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "bibliomantic_consultationArguments",
  "type": "object"
}
```

#### get_hexagram_details

**Description**: 
    Enhanced hexagram details with traditional Chinese names, Unicode symbols, and rich commentary.
    MAINTAINS BACKWARD COMPATIBILITY while dramatically improving content quality.
    

**Input Parameters**:
```json
{
  "properties": {
    "hexagram_number": {
      "title": "Hexagram Number",
      "type": "integer"
    }
  },
  "required": [
    "hexagram_number"
  ],
  "title": "get_hexagram_detailsArguments",
  "type": "object"
}
```

#### server_statistics

**Description**: Enhanced server statistics

**Input Parameters**:
```json
{
  "properties": {},
  "title": "server_statisticsArguments",
  "type": "object"
}
```

---

###  BioMCP

**Description**: 

**Connection Status**: success

**Available Tools** (35 ):

#### search

**Description**: Search biomedical literature, clinical trials, genetic variants, genes, drugs, and diseases.

    ⚠️ IMPORTANT: Have you used the 'think' tool first? If not, STOP and use it NOW!
    The 'think' tool is REQUIRED for proper research planning and should be your FIRST step.

    This tool provides access to biomedical data from PubMed/PubTator3, ClinicalTrials.gov,
    MyVariant.info, and the BioThings suite (MyGene.info, MyChem.info, MyDisease.info).
    It supports two search modes:

    ## 1. UNIFIED QUERY LANGUAGE
    Use the 'query' parameter with field-based syntax for precise cross-domain searches.

    Syntax:
    - Basic: "gene:BRAF"
    - AND logic: "gene:BRAF AND disease:melanoma"
    - OR logic: "gene:PTEN AND (R173 OR Arg173 OR 'position 173')"
    - Domain-specific: "trials.condition:melanoma AND trials.phase:3"

    Common fields:
    - Cross-domain: gene, disease, variant, chemical/drug
    - Articles: pmid, title, abstract, journal, author
    - Trials: trials.condition, trials.intervention, trials.phase, trials.status
    - Variants: variants.hgvs, variants.rsid, variants.significance

    Example:
    ```
    await search(
        query="gene:BRAF AND disease:melanoma AND trials.phase:3",
        max_results_per_domain=20
    )
    ```

    ## 2. DOMAIN-SPECIFIC SEARCH
    Use the 'domain' parameter with specific filters for targeted searches.

    Domains:
    - "article": Search PubMed/PubTator3 for research articles and preprints ABOUT genes, variants, diseases, or chemicals
    - "trial": Search ClinicalTrials.gov for clinical studies
    - "variant": Search MyVariant.info for genetic variant DATABASE RECORDS (population frequency, clinical significance, etc.) - NOT for articles about variants!
    - "gene": Search MyGene.info for gene information (symbol, name, function, aliases)
    - "drug": Search MyChem.info for drug/chemical information (names, formulas, indications)
    - "disease": Search MyDisease.info for disease information (names, definitions, synonyms)
    - "nci_organization": Search NCI database for cancer centers, hospitals, and research sponsors (requires API key)
    - "nci_intervention": Search NCI database for drugs, devices, procedures used in cancer trials (requires API key)
    - "nci_biomarker": Search NCI database for biomarkers used in trial eligibility criteria (requires API key)
    - "nci_disease": Search NCI controlled vocabulary for cancer conditions and terms (requires API key)

    Example:
    ```
    await search(
        domain="article",
        genes=["BRAF", "NRAS"],
        diseases=["melanoma"],
        page_size=50
    )
    ```

    ## DOMAIN SELECTION EXAMPLES:
    - To find ARTICLES about BRAF V600E mutation: domain="article", genes=["BRAF"], variants=["V600E"]
    - To find VARIANT DATA for BRAF mutations: domain="variant", gene="BRAF"
    - To find articles about ERBB2 p.D277Y: domain="article", genes=["ERBB2"], variants=["p.D277Y"]
    - Common mistake: Using domain="variant" when you want articles about a variant

    ## IMPORTANT NOTES:
    - For complex research questions, use the separate 'think' tool for systematic analysis
    - The tool returns results in OpenAI MCP format: {"results": [{"id", "title", "text", "url"}, ...]}
    - Search results do NOT include metadata (per OpenAI MCP specification)
    - Use the fetch tool to get detailed metadata for specific records
    - Use get_schema=True to explore available search fields
    - Use explain_query=True to understand query parsing (unified mode)
    - Domain-specific searches use AND logic for multiple values
    - For OR logic, use the unified query language
    - NEW: Article search keywords support OR with pipe separator: "R173|Arg173|p.R173"
    - Remember: domain="article" finds LITERATURE, domain="variant" finds DATABASE RECORDS

    ## RETURN FORMAT:
    All search modes return results in this format:
    ```json
    {
        "results": [
            {
                "id": "unique_identifier",
                "title": "Human-readable title",
                "text": "Summary or snippet of content",
                "url": "Link to full resource"
            }
        ]
    }
    ```
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "call_benefit": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Brief explanation of why this search is being performed and expected benefit. Helps improve search accuracy and provides context for analytics. Highly recommended for better results.",
      "title": "Call Benefit"
    },
    "domain": {
      "anyOf": [
        {
          "enum": [
            "article",
            "trial",
            "variant",
            "gene",
            "drug",
            "disease",
            "nci_organization",
            "nci_intervention",
            "nci_biomarker",
            "nci_disease",
            "fda_adverse",
            "fda_label",
            "fda_device",
            "fda_approval",
            "fda_recall",
            "fda_shortage"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Domain to search: 'article' for papers/literature ABOUT genes/variants/diseases, 'trial' for clinical studies, 'variant' for genetic variant DATABASE RECORDS, 'gene' for gene information from MyGene.info, 'drug' for drug/chemical information from MyChem.info, 'disease' for disease information from MyDisease.info, 'nci_organization' for NCI cancer centers/sponsors, 'nci_intervention' for NCI drugs/devices/procedures, 'nci_biomarker' for NCI trial eligibility biomarkers, 'nci_disease' for NCI cancer vocabulary, 'fda_adverse' for FDA adverse event reports, 'fda_label' for FDA drug labels, 'fda_device' for FDA device events, 'fda_approval' for FDA drug approvals, 'fda_recall' for FDA drug recalls, 'fda_shortage' for FDA drug shortages",
      "title": "Domain"
    },
    "genes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Genes"
    },
    "diseases": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Diseases"
    },
    "variants": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Variants"
    },
    "chemicals": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Chemicals"
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Keywords"
    },
    "conditions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Conditions"
    },
    "interventions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Interventions"
    },
    "recruiting_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Recruiting Status"
    },
    "phase": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Phase"
    },
    "significance": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Significance"
    },
    "lat": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lat"
    },
    "long": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Long"
    },
    "distance": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Distance"
    },
    "page": {
      "default": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 10,
      "title": "Page Size",
      "type": "integer"
    },
    "max_results_per_domain": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Max Results Per Domain"
    },
    "explain_query": {
      "default": false,
      "title": "Explain Query",
      "type": "boolean"
    },
    "get_schema": {
      "default": false,
      "title": "Get Schema",
      "type": "boolean"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key for searching NCI domains (nci_organization, nci_intervention, nci_biomarker, nci_disease). Required for NCI searches. Get a free key at: https://clinicaltrialsapi.cancer.gov/",
      "title": "Api Key"
    }
  },
  "required": [
    "query"
  ],
  "title": "searchArguments",
  "type": "object"
}
```

#### fetch

**Description**: Fetch comprehensive details for a specific biomedical record.

    This tool retrieves full information for articles, clinical trials, genetic variants,
    genes, drugs, or diseases using their unique identifiers. It returns data in a
    standardized format suitable for detailed analysis and research.

    ## IDENTIFIER FORMATS:
    - Articles: PMID (PubMed ID) - e.g., "35271234" OR DOI - e.g., "10.1101/2024.01.20.23288905"
    - Trials: NCT ID (ClinicalTrials.gov ID) - e.g., "NCT04280705"
    - Variants: HGVS notation or dbSNP ID - e.g., "chr7:g.140453136A>T" or "rs121913254"
    - Genes: Gene symbol or Entrez ID - e.g., "BRAF" or "673"
    - Drugs: Drug name or ID - e.g., "imatinib" or "DB00619"
    - Diseases: Disease name or ID - e.g., "melanoma" or "MONDO:0005105"
    - NCI Organizations: NCI organization ID - e.g., "NCI-2011-03337"
    - NCI Interventions: NCI intervention ID - e.g., "INT123456"
    - NCI Diseases: NCI disease ID - e.g., "C4872"

    The domain is automatically detected from the ID format if not provided:
    - NCT* → trial
    - Contains "/" with numeric prefix (DOI) → article
    - Pure numeric → article (PMID)
    - rs* or contains ':' or 'g.' → variant
    - For genes, drugs, diseases: manual specification recommended

    ## DOMAIN-SPECIFIC OPTIONS:

    ### Articles (domain="article"):
    - Returns full article metadata, abstract, and full text when available
    - Supports both PubMed articles (via PMID) and Europe PMC preprints (via DOI)
    - Includes annotations for genes, diseases, chemicals, and variants (PubMed only)
    - detail="full" attempts to retrieve full text content (PubMed only)

    ### Clinical Trials (domain="trial"):
    - detail=None or "protocol": Core study information
    - detail="locations": Study sites and contact information
    - detail="outcomes": Primary/secondary outcomes and results
    - detail="references": Related publications and citations
    - detail="all": Complete trial record with all sections

    ### Variants (domain="variant"):
    - Returns comprehensive variant information including:
      - Clinical significance and interpretations
      - Population frequencies
      - Gene/protein effects
      - External database links
    - detail parameter is ignored (always returns full data)

    ### Genes (domain="gene"):
    - Returns gene information from MyGene.info including:
      - Gene symbol, name, and type
      - Entrez ID and Ensembl IDs
      - Gene summary and aliases
      - RefSeq information
    - detail parameter is ignored (always returns full data)

    ### Drugs (domain="drug"):
    - Returns drug/chemical information from MyChem.info including:
      - Drug name and trade names
      - Chemical formula and structure IDs
      - Clinical indications
      - Mechanism of action
      - External database links (DrugBank, PubChem, ChEMBL)
    - detail parameter is ignored (always returns full data)

    ### Diseases (domain="disease"):
    - Returns disease information from MyDisease.info including:
      - Disease name and definition
      - MONDO ontology ID
      - Disease synonyms
      - Cross-references to other databases
      - Associated phenotypes
    - detail parameter is ignored (always returns full data)

    ### NCI Organizations (domain="nci_organization"):
    - Returns organization information from NCI database including:
      - Organization name and type
      - Full address and contact information
      - Research focus areas
      - Associated clinical trials
    - Requires NCI API key
    - detail parameter is ignored (always returns full data)

    ### NCI Interventions (domain="nci_intervention"):
    - Returns intervention information from NCI database including:
      - Intervention name and type
      - Synonyms and alternative names
      - Mechanism of action (for drugs)
      - FDA approval status
      - Associated clinical trials
    - Requires NCI API key
    - detail parameter is ignored (always returns full data)

    ### NCI Diseases (domain="nci_disease"):
    - Returns disease information from NCI controlled vocabulary including:
      - Preferred disease name
      - Disease category and classification
      - All known synonyms
      - Cross-reference codes (ICD, SNOMED)
    - Requires NCI API key
    - detail parameter is ignored (always returns full data)

    ## RETURN FORMAT:
    All fetch operations return a standardized format:
    ```json
    {
        "id": "unique_identifier",
        "title": "Record title or name",
        "text": "Full content or comprehensive description",
        "url": "Link to original source",
        "metadata": {
            // Domain-specific additional fields
        }
    }
    ```

    ## EXAMPLES:

    Fetch article by PMID (domain auto-detected):
    ```
    await fetch(id="35271234")
    ```

    Fetch article by DOI (domain auto-detected):
    ```
    await fetch(id="10.1101/2024.01.20.23288905")
    ```

    Fetch complete trial information (domain auto-detected):
    ```
    await fetch(
        id="NCT04280705",
        detail="all"
    )
    ```

    Fetch variant with clinical interpretations:
    ```
    await fetch(id="rs121913254")
    ```

    Explicitly specify domain (optional):
    ```
    await fetch(
        domain="variant",
        id="chr7:g.140453136A>T"
    )
    ```
    

**Input Parameters**:
```json
{
  "properties": {
    "id": {
      "title": "Id",
      "type": "string"
    },
    "domain": {
      "anyOf": [
        {
          "enum": [
            "article",
            "trial",
            "variant",
            "gene",
            "drug",
            "disease",
            "nci_organization",
            "nci_intervention",
            "nci_biomarker",
            "nci_disease",
            "fda_adverse",
            "fda_label",
            "fda_device",
            "fda_approval",
            "fda_recall",
            "fda_shortage"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Domain of the record (auto-detected if not provided)",
      "title": "Domain"
    },
    "call_benefit": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Brief explanation of why this fetch is being performed and expected benefit. Helps provide context for analytics and improves result relevance.",
      "title": "Call Benefit"
    },
    "detail": {
      "anyOf": [
        {
          "enum": [
            "protocol",
            "locations",
            "outcomes",
            "references",
            "all",
            "full"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Detail"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key for fetching NCI records (nci_organization, nci_intervention, nci_disease). Required for NCI fetches. Get a free key at: https://clinicaltrialsapi.cancer.gov/",
      "title": "Api Key"
    }
  },
  "required": [
    "id"
  ],
  "title": "fetchArguments",
  "type": "object"
}
```

#### think

**Description**: REQUIRED FIRST STEP: Perform structured sequential thinking for ANY biomedical research task.

    🚨 IMPORTANT: You MUST use this tool BEFORE any search or fetch operations when:
    - Researching ANY biomedical topic (genes, diseases, variants, trials)
    - Planning to use multiple BioMCP tools
    - Answering questions that require analysis or synthesis
    - Comparing information from different sources
    - Making recommendations or drawing conclusions

    ⚠️ FAILURE TO USE THIS TOOL FIRST will result in:
    - Incomplete or poorly structured analysis
    - Missing important connections between data
    - Suboptimal search strategies
    - Overlooked critical information

    Sequential thinking ensures you:
    1. Fully understand the research question
    2. Plan an optimal search strategy
    3. Identify all relevant data sources
    4. Structure your analysis properly
    5. Deliver comprehensive, well-reasoned results

    ## Usage Pattern:
    1. Start with thoughtNumber=1 to initiate analysis
    2. Progress through numbered thoughts sequentially
    3. Adjust totalThoughts estimate as understanding develops
    4. Set nextThoughtNeeded=False only when analysis is complete

    ## Example:
    ```python
    # Initial analysis
    await think(
        thought="Breaking down the relationship between BRAF mutations and melanoma treatment resistance...",
        thoughtNumber=1,
        totalThoughts=5,
        nextThoughtNeeded=True
    )

    # Continue analysis
    await think(
        thought="Examining specific BRAF V600E mutation mechanisms...",
        thoughtNumber=2,
        totalThoughts=5,
        nextThoughtNeeded=True
    )

    # Final thought
    await think(
        thought="Synthesizing findings and proposing research directions...",
        thoughtNumber=5,
        totalThoughts=5,
        nextThoughtNeeded=False
    )
    ```

    ## Important Notes:
    - Each thought builds on previous ones within a session
    - State is maintained throughout the MCP session
    - Use thoughtful, detailed analysis in each step
    - Revisions and branching are supported through the underlying implementation
    

**Input Parameters**:
```json
{
  "properties": {
    "thought": {
      "description": "Current thinking step for analysis",
      "title": "Thought",
      "type": "string"
    },
    "thoughtNumber": {
      "description": "Current thought number, starting at 1",
      "minimum": 1,
      "title": "Thoughtnumber",
      "type": "integer"
    },
    "totalThoughts": {
      "description": "Estimated total thoughts needed for complete analysis",
      "minimum": 1,
      "title": "Totalthoughts",
      "type": "integer"
    },
    "nextThoughtNeeded": {
      "default": true,
      "description": "Whether more thinking steps are needed after this one",
      "title": "Nextthoughtneeded",
      "type": "boolean"
    }
  },
  "required": [
    "thought",
    "thoughtNumber",
    "totalThoughts"
  ],
  "title": "thinkArguments",
  "type": "object"
}
```

#### article_searcher

**Description**: Search PubMed/PubTator3 for research articles and preprints.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Use this tool to find scientific literature ABOUT genes, variants, diseases, or chemicals.
    Results include articles from PubMed and optionally preprints from bioRxiv/medRxiv.

    Important: This searches for ARTICLES ABOUT these topics, not database records.
    For genetic variant database records, use variant_searcher instead.

    Example usage:
    - Find articles about BRAF mutations in melanoma
    - Search for papers on a specific drug's effects
    - Locate research on gene-disease associations
    

**Input Parameters**:
```json
{
  "properties": {
    "chemicals": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Chemical/drug names to search for",
      "title": "Chemicals"
    },
    "diseases": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Disease names to search for",
      "title": "Diseases"
    },
    "genes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gene symbols to search for",
      "title": "Genes"
    },
    "keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Free-text keywords to search for",
      "title": "Keywords"
    },
    "variants": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Variant strings to search for (e.g., 'V600E', 'p.D277Y')",
      "title": "Variants"
    },
    "include_preprints": {
      "default": true,
      "description": "Include preprints from bioRxiv/medRxiv",
      "title": "Include Preprints",
      "type": "boolean"
    },
    "include_cbioportal": {
      "default": true,
      "description": "Include cBioPortal cancer genomics summary when searching by gene",
      "title": "Include Cbioportal",
      "type": "boolean"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 10,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "article_searcherArguments",
  "type": "object"
}
```

#### article_getter

**Description**: Fetch detailed information for a specific article.

    Retrieves the full abstract and available text for an article by its identifier.
    Supports:
    - PubMed IDs (PMID) for published articles
    - PMC IDs for articles in PubMed Central
    - DOIs for preprints from Europe PMC

    Returns formatted text including:
    - Title
    - Abstract
    - Full text (when available from PMC for published articles)
    - Source information (PubMed or Europe PMC)
    

**Input Parameters**:
```json
{
  "properties": {
    "pmid": {
      "description": "Article identifier - either a PubMed ID (e.g., '38768446' or 'PMC11193658') or DOI (e.g., '10.1101/2024.01.20.23288905')",
      "title": "Pmid",
      "type": "string"
    }
  },
  "required": [
    "pmid"
  ],
  "title": "article_getterArguments",
  "type": "object"
}
```

#### trial_searcher

**Description**: Search ClinicalTrials.gov for clinical studies.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Comprehensive search tool for finding clinical trials based on multiple criteria.
    Supports filtering by conditions, interventions, location, phase, and eligibility.

    Location search notes:
    - Use either location term OR lat/long coordinates, not both
    - For city-based searches, AI agents should geocode to lat/long first
    - Distance parameter only works with lat/long coordinates

    Returns a formatted list of matching trials with key details.
    

**Input Parameters**:
```json
{
  "properties": {
    "conditions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Medical conditions to search for",
      "title": "Conditions"
    },
    "interventions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Treatment interventions to search for",
      "title": "Interventions"
    },
    "other_terms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Additional search terms",
      "title": "Other Terms"
    },
    "recruiting_status": {
      "anyOf": [
        {
          "enum": [
            "OPEN",
            "CLOSED",
            "ANY"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by recruiting status",
      "title": "Recruiting Status"
    },
    "phase": {
      "anyOf": [
        {
          "enum": [
            "EARLY_PHASE1",
            "PHASE1",
            "PHASE2",
            "PHASE3",
            "PHASE4",
            "NOT_APPLICABLE"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by clinical trial phase",
      "title": "Phase"
    },
    "location": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Location term for geographic filtering",
      "title": "Location"
    },
    "lat": {
      "anyOf": [
        {
          "maximum": 90.0,
          "minimum": -90.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Latitude for location-based search. AI agents should geocode city names before using.",
      "title": "Lat"
    },
    "long": {
      "anyOf": [
        {
          "maximum": 180.0,
          "minimum": -180.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Longitude for location-based search. AI agents should geocode city names before using.",
      "title": "Long"
    },
    "distance": {
      "anyOf": [
        {
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Distance in miles from lat/long coordinates",
      "title": "Distance"
    },
    "age_group": {
      "anyOf": [
        {
          "enum": [
            "CHILD",
            "ADULT",
            "OLDER_ADULT"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by age group",
      "title": "Age Group"
    },
    "sex": {
      "anyOf": [
        {
          "enum": [
            "FEMALE",
            "MALE",
            "ALL"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by biological sex",
      "title": "Sex"
    },
    "healthy_volunteers": {
      "anyOf": [
        {
          "enum": [
            "YES",
            "NO"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by healthy volunteer eligibility",
      "title": "Healthy Volunteers"
    },
    "study_type": {
      "anyOf": [
        {
          "enum": [
            "INTERVENTIONAL",
            "OBSERVATIONAL",
            "EXPANDED_ACCESS"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by study type",
      "title": "Study Type"
    },
    "funder_type": {
      "anyOf": [
        {
          "enum": [
            "NIH",
            "OTHER_GOV",
            "INDUSTRY",
            "OTHER"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by funding source",
      "title": "Funder Type"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 10,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "trial_searcherArguments",
  "type": "object"
}
```

#### trial_getter

**Description**: Fetch comprehensive details for a specific clinical trial.

    Retrieves all available information for a clinical trial by its NCT ID.
    This includes protocol details, locations, outcomes, and references.

    For specific sections only, use the specialized getter tools:
    - trial_protocol_getter: Core protocol information
    - trial_locations_getter: Site locations and contacts
    - trial_outcomes_getter: Primary/secondary outcomes and results
    - trial_references_getter: Publications and references
    

**Input Parameters**:
```json
{
  "properties": {
    "nct_id": {
      "description": "NCT ID (e.g., 'NCT06524388')",
      "title": "Nct Id",
      "type": "string"
    }
  },
  "required": [
    "nct_id"
  ],
  "title": "trial_getterArguments",
  "type": "object"
}
```

#### trial_protocol_getter

**Description**: Fetch core protocol information for a clinical trial.

    Retrieves essential protocol details including:
    - Official title and brief summary
    - Study status and sponsor information
    - Study design (type, phase, allocation, masking)
    - Eligibility criteria
    - Primary completion date
    

**Input Parameters**:
```json
{
  "properties": {
    "nct_id": {
      "description": "NCT ID (e.g., 'NCT06524388')",
      "title": "Nct Id",
      "type": "string"
    }
  },
  "required": [
    "nct_id"
  ],
  "title": "trial_protocol_getterArguments",
  "type": "object"
}
```

#### trial_references_getter

**Description**: Fetch publications and references for a clinical trial.

    Retrieves all linked publications including:
    - Published results papers
    - Background literature
    - Protocol publications
    - Related analyses

    Includes PubMed IDs when available for easy cross-referencing.
    

**Input Parameters**:
```json
{
  "properties": {
    "nct_id": {
      "description": "NCT ID (e.g., 'NCT06524388')",
      "title": "Nct Id",
      "type": "string"
    }
  },
  "required": [
    "nct_id"
  ],
  "title": "trial_references_getterArguments",
  "type": "object"
}
```

#### trial_outcomes_getter

**Description**: Fetch outcome measures and results for a clinical trial.

    Retrieves detailed outcome information including:
    - Primary outcome measures
    - Secondary outcome measures
    - Results data (if available)
    - Adverse events (if reported)

    Note: Results are only available for completed trials that have posted data.
    

**Input Parameters**:
```json
{
  "properties": {
    "nct_id": {
      "description": "NCT ID (e.g., 'NCT06524388')",
      "title": "Nct Id",
      "type": "string"
    }
  },
  "required": [
    "nct_id"
  ],
  "title": "trial_outcomes_getterArguments",
  "type": "object"
}
```

#### trial_locations_getter

**Description**: Fetch contact and location details for a clinical trial.

    Retrieves all study locations including:
    - Facility names and addresses
    - Principal investigator information
    - Contact details (when recruiting)
    - Recruitment status by site

    Useful for finding trials near specific locations or contacting study teams.
    

**Input Parameters**:
```json
{
  "properties": {
    "nct_id": {
      "description": "NCT ID (e.g., 'NCT06524388')",
      "title": "Nct Id",
      "type": "string"
    }
  },
  "required": [
    "nct_id"
  ],
  "title": "trial_locations_getterArguments",
  "type": "object"
}
```

#### variant_searcher

**Description**: Search MyVariant.info for genetic variant DATABASE RECORDS.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Important: This searches for variant DATABASE RECORDS (frequency, significance, etc.),
    NOT articles about variants. For articles about variants, use article_searcher.

    Searches the comprehensive variant database including:
    - Population frequencies (gnomAD, 1000 Genomes, etc.)
    - Clinical significance (ClinVar)
    - Functional predictions (SIFT, PolyPhen, CADD)
    - Gene and protein consequences

    Search by various identifiers or filter by clinical/functional criteria.
    

**Input Parameters**:
```json
{
  "properties": {
    "gene": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gene symbol (e.g., 'BRAF', 'TP53')",
      "title": "Gene"
    },
    "hgvs": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "HGVS notation (genomic, coding, or protein)",
      "title": "Hgvs"
    },
    "hgvsp": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Protein change in HGVS format (e.g., 'p.V600E')",
      "title": "Hgvsp"
    },
    "hgvsc": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Coding sequence change (e.g., 'c.1799T>A')",
      "title": "Hgvsc"
    },
    "rsid": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "dbSNP rsID (e.g., 'rs113488022')",
      "title": "Rsid"
    },
    "region": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Genomic region (e.g., 'chr7:140753336-140753337')",
      "title": "Region"
    },
    "significance": {
      "anyOf": [
        {
          "enum": [
            "pathogenic",
            "likely_pathogenic",
            "uncertain_significance",
            "likely_benign",
            "benign",
            "conflicting"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Clinical significance filter",
      "title": "Significance"
    },
    "frequency_min": {
      "anyOf": [
        {
          "maximum": 1.0,
          "minimum": 0.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Minimum allele frequency",
      "title": "Frequency Min"
    },
    "frequency_max": {
      "anyOf": [
        {
          "maximum": 1.0,
          "minimum": 0.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Maximum allele frequency",
      "title": "Frequency Max"
    },
    "consequence": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Variant consequence (e.g., 'missense_variant')",
      "title": "Consequence"
    },
    "cadd_score_min": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Minimum CADD score for pathogenicity",
      "title": "Cadd Score Min"
    },
    "sift_prediction": {
      "anyOf": [
        {
          "enum": [
            "deleterious",
            "tolerated"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "SIFT functional prediction",
      "title": "Sift Prediction"
    },
    "polyphen_prediction": {
      "anyOf": [
        {
          "enum": [
            "probably_damaging",
            "possibly_damaging",
            "benign"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "PolyPhen-2 functional prediction",
      "title": "Polyphen Prediction"
    },
    "include_cbioportal": {
      "default": true,
      "description": "Include cBioPortal cancer genomics summary when searching by gene",
      "title": "Include Cbioportal",
      "type": "boolean"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 10,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "variant_searcherArguments",
  "type": "object"
}
```

#### variant_getter

**Description**: Fetch comprehensive details for a specific genetic variant.

    Retrieves all available information for a variant including:
    - Gene location and consequences
    - Population frequencies across databases
    - Clinical significance from ClinVar
    - Functional predictions
    - External annotations (TCGA cancer data, conservation scores)

    Accepts various ID formats:
    - HGVS: NM_004333.4:c.1799T>A
    - rsID: rs113488022
    - MyVariant ID: chr7:g.140753336A>T
    

**Input Parameters**:
```json
{
  "properties": {
    "variant_id": {
      "description": "Variant ID (HGVS, rsID, or MyVariant ID like 'chr7:g.140753336A>T')",
      "title": "Variant Id",
      "type": "string"
    },
    "include_external": {
      "default": true,
      "description": "Include external annotations (TCGA, 1000 Genomes, functional predictions)",
      "title": "Include External",
      "type": "boolean"
    }
  },
  "required": [
    "variant_id"
  ],
  "title": "variant_getterArguments",
  "type": "object"
}
```

#### alphagenome_predictor

**Description**: Predict variant effects on gene regulation using Google DeepMind's AlphaGenome.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your analysis strategy!

    AlphaGenome provides state-of-the-art predictions for how genetic variants
    affect gene regulation, including:
    - Gene expression changes (RNA-seq)
    - Chromatin accessibility impacts (ATAC-seq, DNase-seq)
    - Splicing alterations
    - Promoter activity changes (CAGE)

    This tool requires:
    1. AlphaGenome to be installed (see error message for instructions)
    2. An API key from https://deepmind.google.com/science/alphagenome

    API Key Options:
    - Provide directly via the api_key parameter
    - Or set ALPHAGENOME_API_KEY environment variable

    Example usage:
    - Predict regulatory effects of BRAF V600E mutation: chr7:140753336 A>T
    - Assess non-coding variant impact on gene expression
    - Evaluate promoter variants in specific tissues

    Note: This is an optional tool that enhances variant interpretation
    with AI predictions. Standard annotations remain available via variant_getter.
    

**Input Parameters**:
```json
{
  "properties": {
    "chromosome": {
      "description": "Chromosome (e.g., 'chr7', 'chrX')",
      "title": "Chromosome",
      "type": "string"
    },
    "position": {
      "description": "1-based genomic position of the variant",
      "title": "Position",
      "type": "integer"
    },
    "reference": {
      "description": "Reference allele(s) (e.g., 'A', 'ATG')",
      "title": "Reference",
      "type": "string"
    },
    "alternate": {
      "description": "Alternate allele(s) (e.g., 'T', 'A')",
      "title": "Alternate",
      "type": "string"
    },
    "interval_size": {
      "default": 131072,
      "description": "Size of genomic interval to analyze in bp (max 1,000,000)",
      "maximum": 1000000,
      "minimum": 2000,
      "title": "Interval Size",
      "type": "integer"
    },
    "tissue_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "UBERON ontology terms for tissue-specific predictions (e.g., 'UBERON:0002367' for external ear)",
      "title": "Tissue Types"
    },
    "significance_threshold": {
      "default": 0.5,
      "description": "Threshold for significant log2 fold changes (default: 0.5)",
      "maximum": 5.0,
      "minimum": 0.0,
      "title": "Significance Threshold",
      "type": "number"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "AlphaGenome API key. Check if user mentioned 'my AlphaGenome API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    }
  },
  "required": [
    "chromosome",
    "position",
    "reference",
    "alternate"
  ],
  "title": "alphagenome_predictorArguments",
  "type": "object"
}
```

#### gene_getter

**Description**: Get detailed gene information from MyGene.info.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to understand your research goal!

    Provides real-time gene annotations including:
    - Official gene name and symbol
    - Gene summary/description
    - Aliases and alternative names
    - Gene type (protein-coding, etc.)
    - Links to external databases

    This tool fetches CURRENT gene information from MyGene.info, ensuring
    you always have the latest annotations and nomenclature.

    Example usage:
    - Get information about TP53 tumor suppressor
    - Look up BRAF kinase gene details
    - Find the official name for a gene by its alias

    Note: For genetic variants, use variant_searcher. For articles about genes, use article_searcher.
    

**Input Parameters**:
```json
{
  "properties": {
    "gene_id_or_symbol": {
      "description": "Gene symbol (e.g., 'TP53', 'BRAF') or Entrez ID (e.g., '7157')",
      "title": "Gene Id Or Symbol",
      "type": "string"
    }
  },
  "required": [
    "gene_id_or_symbol"
  ],
  "title": "gene_getterArguments",
  "type": "object"
}
```

#### disease_getter

**Description**: Get detailed disease information from MyDisease.info.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to understand your research goal!

    Provides real-time disease annotations including:
    - Official disease name and definition
    - Disease synonyms and alternative names
    - Ontology mappings (MONDO, DOID, OMIM, etc.)
    - Associated phenotypes
    - Links to disease databases

    This tool fetches CURRENT disease information from MyDisease.info, ensuring
    you always have the latest ontology mappings and definitions.

    Example usage:
    - Get the definition of GIST (Gastrointestinal Stromal Tumor)
    - Look up synonyms for melanoma
    - Find the MONDO ID for a disease by name

    Note: For clinical trials about diseases, use trial_searcher. For articles about diseases, use article_searcher.
    

**Input Parameters**:
```json
{
  "properties": {
    "disease_id_or_name": {
      "description": "Disease name (e.g., 'melanoma', 'lung cancer') or ontology ID (e.g., 'MONDO:0016575', 'DOID:1909')",
      "title": "Disease Id Or Name",
      "type": "string"
    }
  },
  "required": [
    "disease_id_or_name"
  ],
  "title": "disease_getterArguments",
  "type": "object"
}
```

#### drug_getter

**Description**: Get detailed drug/chemical information from MyChem.info.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to understand your research goal!

    This tool provides comprehensive drug information including:
    - Chemical properties (formula, InChIKey)
    - Drug identifiers (DrugBank, ChEMBL, PubChem)
    - Trade names and brand names
    - Clinical indications
    - Mechanism of action
    - Pharmacology details
    - Links to drug databases

    This tool fetches CURRENT drug information from MyChem.info, part of the
    BioThings suite, ensuring you always have the latest drug data.

    Example usage:
    - Get information about imatinib (Gleevec)
    - Look up details for DrugBank ID DB00619
    - Find the mechanism of action for pembrolizumab

    Note: For clinical trials about drugs, use trial_searcher. For articles about drugs, use article_searcher.
    

**Input Parameters**:
```json
{
  "properties": {
    "drug_id_or_name": {
      "description": "Drug name (e.g., 'aspirin', 'imatinib') or ID (e.g., 'DB00945', 'CHEMBL941')",
      "title": "Drug Id Or Name",
      "type": "string"
    }
  },
  "required": [
    "drug_id_or_name"
  ],
  "title": "drug_getterArguments",
  "type": "object"
}
```

#### nci_organization_searcher

**Description**: Search for organizations in the NCI Clinical Trials database.

    Searches the National Cancer Institute's curated database of organizations
    involved in cancer clinical trials. This includes:
    - Academic medical centers
    - Community hospitals
    - Industry sponsors
    - Government facilities
    - Research networks

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    IMPORTANT: To avoid API errors, always use city AND state together when searching by location.
    The NCI API has limitations on broad searches.

    Example usage:
    - Find cancer centers in Boston, MA (city AND state)
    - Search for "MD Anderson" in Houston, TX
    - List academic organizations in Cleveland, OH
    - Search by organization name alone (without location)
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Organization name to search for (partial match supported)",
      "title": "Name"
    },
    "organization_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Type of organization (e.g., 'Academic', 'Industry', 'Government')",
      "title": "Organization Type"
    },
    "city": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "City where organization is located. IMPORTANT: Always use with state to avoid API errors",
      "title": "City"
    },
    "state": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "State/province code (e.g., 'CA', 'NY'). IMPORTANT: Always use with city to avoid API errors",
      "title": "State"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 20,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "nci_organization_searcherArguments",
  "type": "object"
}
```

#### nci_organization_getter

**Description**: Get detailed information about a specific organization from NCI.

    Retrieves comprehensive details about an organization including:
    - Full name and aliases
    - Address and contact information
    - Organization type and role
    - Associated clinical trials
    - Research focus areas

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    Example usage:
    - Get details about a specific cancer center
    - Find contact information for trial sponsors
    - View organization's trial portfolio
    

**Input Parameters**:
```json
{
  "properties": {
    "organization_id": {
      "description": "NCI organization ID (e.g., 'NCI-2011-03337')",
      "title": "Organization Id",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    }
  },
  "required": [
    "organization_id"
  ],
  "title": "nci_organization_getterArguments",
  "type": "object"
}
```

#### nci_intervention_searcher

**Description**: Search for interventions in the NCI Clinical Trials database.

    Searches the National Cancer Institute's curated database of interventions
    used in cancer clinical trials. This includes:
    - FDA-approved drugs
    - Investigational agents
    - Medical devices
    - Surgical procedures
    - Radiation therapies
    - Behavioral interventions

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    Example usage:
    - Find all trials using pembrolizumab
    - Search for CAR-T cell therapies
    - List radiation therapy protocols
    - Find dietary interventions
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Intervention name to search for (e.g., 'pembrolizumab')",
      "title": "Name"
    },
    "intervention_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Type of intervention: 'Drug', 'Device', 'Biological', 'Procedure', 'Radiation', 'Behavioral', 'Genetic', 'Dietary', 'Other'",
      "title": "Intervention Type"
    },
    "synonyms": {
      "default": true,
      "description": "Include synonym matches in search",
      "title": "Synonyms",
      "type": "boolean"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "anyOf": [
        {
          "maximum": 100,
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Results per page. If not specified, returns all matching results.",
      "title": "Page Size"
    }
  },
  "title": "nci_intervention_searcherArguments",
  "type": "object"
}
```

#### nci_intervention_getter

**Description**: Get detailed information about a specific intervention from NCI.

    Retrieves comprehensive details about an intervention including:
    - Full name and synonyms
    - Intervention type and category
    - Mechanism of action (for drugs)
    - FDA approval status
    - Associated clinical trials
    - Combination therapies

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    Example usage:
    - Get details about a specific drug
    - Find all trials using a device
    - View combination therapy protocols
    

**Input Parameters**:
```json
{
  "properties": {
    "intervention_id": {
      "description": "NCI intervention ID (e.g., 'INT123456')",
      "title": "Intervention Id",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    }
  },
  "required": [
    "intervention_id"
  ],
  "title": "nci_intervention_getterArguments",
  "type": "object"
}
```

#### nci_biomarker_searcher

**Description**: Search for biomarkers in the NCI Clinical Trials database.

    Searches for biomarkers used in clinical trial eligibility criteria.
    This is essential for precision medicine trials that select patients
    based on specific biomarker characteristics.

    Biomarker examples:
    - Gene mutations (e.g., BRAF V600E, EGFR T790M)
    - Protein expression (e.g., PD-L1 ≥ 50%, HER2 positive)
    - Gene fusions (e.g., ALK fusion, ROS1 fusion)
    - Other molecular markers (e.g., MSI-H, TMB-high)

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    Note: Biomarker data availability may be limited in CTRP.
    Results focus on biomarkers used in trial eligibility criteria.

    Example usage:
    - Search for PD-L1 expression biomarkers
    - Find trials requiring EGFR mutations
    - Look up biomarkers tested by NGS
    - Search for HER2 expression markers
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Biomarker name to search for (e.g., 'PD-L1', 'EGFR mutation')",
      "title": "Name"
    },
    "biomarker_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Type of biomarker ('reference_gene' or 'branch')",
      "title": "Biomarker Type"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 20,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "nci_biomarker_searcherArguments",
  "type": "object"
}
```

#### nci_disease_searcher

**Description**: Search NCI's controlled vocabulary of cancer conditions.

    Searches the National Cancer Institute's curated database of cancer
    conditions and diseases used in clinical trials. This is different from
    the general disease_getter tool which uses MyDisease.info.

    NCI's disease vocabulary provides:
    - Official cancer terminology used in trials
    - Disease synonyms and alternative names
    - Hierarchical disease classifications
    - Standardized disease codes for trial matching

    Requires NCI API key from: https://clinicaltrialsapi.cancer.gov/

    Example usage:
    - Search for specific cancer types (e.g., "melanoma")
    - Find all lung cancer subtypes
    - Look up official names for disease synonyms
    - Get standardized disease terms for trial searches

    Note: This is specifically for NCI's cancer disease vocabulary.
    For general disease information, use the disease_getter tool.
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Disease name to search for (partial match)",
      "title": "Name"
    },
    "include_synonyms": {
      "default": true,
      "description": "Include synonym matches in search",
      "title": "Include Synonyms",
      "type": "boolean"
    },
    "category": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Disease category/type filter",
      "title": "Category"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NCI API key. Check if user mentioned 'my NCI API key is...' in their message. If not provided here and no env var is set, user will be prompted to provide one.",
      "title": "Api Key"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 20,
      "description": "Results per page",
      "maximum": 100,
      "minimum": 1,
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "nci_disease_searcherArguments",
  "type": "object"
}
```

#### openfda_adverse_searcher

**Description**: Search FDA adverse event reports (FAERS) for drug safety information.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Searches FDA's Adverse Event Reporting System for:
    - Drug side effects and adverse reactions
    - Serious event reports (death, hospitalization, disability)
    - Safety signal patterns across patient populations

    Note: These reports do not establish causation - they are voluntary reports
    that may contain incomplete or unverified information.
    

**Input Parameters**:
```json
{
  "properties": {
    "drug": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Drug name to search for adverse events",
      "title": "Drug"
    },
    "reaction": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Adverse reaction term to search for",
      "title": "Reaction"
    },
    "serious": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter for serious events only",
      "title": "Serious"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_adverse_searcherArguments",
  "type": "object"
}
```

#### openfda_adverse_getter

**Description**: Get detailed information for a specific FDA adverse event report.

    Retrieves complete details including:
    - Patient demographics and medical history
    - All drugs involved and dosages
    - Complete list of adverse reactions
    - Event narrative and outcomes
    - Reporter information
    

**Input Parameters**:
```json
{
  "properties": {
    "report_id": {
      "description": "Safety report ID",
      "title": "Report Id",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "report_id"
  ],
  "title": "openfda_adverse_getterArguments",
  "type": "object"
}
```

#### openfda_label_searcher

**Description**: Search FDA drug product labels (SPL) for prescribing information.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Searches official FDA drug labels for:
    - Approved indications and usage
    - Dosage and administration guidelines
    - Contraindications and warnings
    - Drug interactions and adverse reactions
    - Special population considerations

    Label sections include: indications, dosage, contraindications, warnings,
    adverse, interactions, pregnancy, pediatric, geriatric, overdose
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Drug name to search for",
      "title": "Name"
    },
    "indication": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Search for drugs indicated for this condition",
      "title": "Indication"
    },
    "boxed_warning": {
      "default": false,
      "description": "Filter for drugs with boxed warnings",
      "title": "Boxed Warning",
      "type": "boolean"
    },
    "section": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Specific label section (e.g., 'contraindications', 'warnings')",
      "title": "Section"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_label_searcherArguments",
  "type": "object"
}
```

#### openfda_label_getter

**Description**: Get complete FDA drug label information by set ID.

    Retrieves the full prescribing information including:
    - Complete indications and usage text
    - Detailed dosing instructions
    - All warnings and precautions
    - Clinical pharmacology and studies
    - Manufacturing and storage information

    Specify sections to retrieve specific parts, or leave empty for default key sections.
    

**Input Parameters**:
```json
{
  "properties": {
    "set_id": {
      "description": "Label set ID",
      "title": "Set Id",
      "type": "string"
    },
    "sections": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Specific sections to retrieve (default: key sections)",
      "title": "Sections"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "set_id"
  ],
  "title": "openfda_label_getterArguments",
  "type": "object"
}
```

#### openfda_device_searcher

**Description**: Search FDA device adverse event reports (MAUDE) for medical device issues.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Searches FDA's device adverse event database for:
    - Device malfunctions and failures
    - Patient injuries related to devices
    - Genomic test and diagnostic device issues

    By default, filters to genomic/diagnostic devices relevant to precision medicine.
    Set genomics_only=False to search all medical devices.
    

**Input Parameters**:
```json
{
  "properties": {
    "device": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Device name to search for",
      "title": "Device"
    },
    "manufacturer": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Manufacturer name",
      "title": "Manufacturer"
    },
    "problem": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Device problem description",
      "title": "Problem"
    },
    "product_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "FDA product code",
      "title": "Product Code"
    },
    "genomics_only": {
      "default": true,
      "description": "Filter to genomic/diagnostic devices only",
      "title": "Genomics Only",
      "type": "boolean"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_device_searcherArguments",
  "type": "object"
}
```

#### openfda_device_getter

**Description**: Get detailed information for a specific FDA device event report.

    Retrieves complete device event details including:
    - Device identification and specifications
    - Complete event narrative
    - Patient outcomes and impacts
    - Manufacturer analysis and actions
    - Remedial actions taken
    

**Input Parameters**:
```json
{
  "properties": {
    "mdr_report_key": {
      "description": "MDR report key",
      "title": "Mdr Report Key",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "mdr_report_key"
  ],
  "title": "openfda_device_getterArguments",
  "type": "object"
}
```

#### openfda_approval_searcher

**Description**: Search FDA drug approval records from Drugs@FDA database.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Returns information about:
    - Application numbers and sponsors
    - Brand and generic names
    - Product formulations and strengths
    - Marketing status and approval dates
    - Submission history

    Useful for verifying if a drug is FDA-approved and when.
    

**Input Parameters**:
```json
{
  "properties": {
    "drug": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Drug name (brand or generic) to search for",
      "title": "Drug"
    },
    "application_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NDA or BLA application number",
      "title": "Application Number"
    },
    "approval_year": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Year of approval (YYYY format)",
      "title": "Approval Year"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_approval_searcherArguments",
  "type": "object"
}
```

#### openfda_approval_getter

**Description**: Get detailed FDA drug approval information for a specific application.

    Returns comprehensive approval details including:
    - Full product list with dosage forms and strengths
    - Complete submission history
    - Marketing status timeline
    - Therapeutic equivalence codes
    - Pharmacologic class information
    

**Input Parameters**:
```json
{
  "properties": {
    "application_number": {
      "description": "NDA or BLA application number",
      "title": "Application Number",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "application_number"
  ],
  "title": "openfda_approval_getterArguments",
  "type": "object"
}
```

#### openfda_recall_searcher

**Description**: Search FDA drug recall records from the Enforcement database.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Returns recall information including:
    - Classification (Class I, II, or III)
    - Recall reason and description
    - Product identification
    - Distribution information
    - Recalling firm details
    - Current status

    Class I = most serious (death/serious harm)
    Class II = moderate (temporary/reversible harm)
    Class III = least serious (unlikely to cause harm)
    

**Input Parameters**:
```json
{
  "properties": {
    "drug": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Drug name to search for recalls",
      "title": "Drug"
    },
    "recall_class": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Recall classification (1=most serious, 2=moderate, 3=least serious)",
      "title": "Recall Class"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Recall status (ongoing, completed, terminated)",
      "title": "Status"
    },
    "reason": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Search text in recall reason",
      "title": "Reason"
    },
    "since_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Show recalls after this date (YYYYMMDD format)",
      "title": "Since Date"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_recall_searcherArguments",
  "type": "object"
}
```

#### openfda_recall_getter

**Description**: Get detailed FDA drug recall information for a specific recall.

    Returns complete recall details including:
    - Full product description and code information
    - Complete reason for recall
    - Distribution pattern and locations
    - Quantity of product recalled
    - Firm information and actions taken
    - Timeline of recall events
    

**Input Parameters**:
```json
{
  "properties": {
    "recall_number": {
      "description": "FDA recall number",
      "title": "Recall Number",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "recall_number"
  ],
  "title": "openfda_recall_getterArguments",
  "type": "object"
}
```

#### openfda_shortage_searcher

**Description**: Search FDA drug shortage records.

    ⚠️ PREREQUISITE: Use the 'think' tool FIRST to plan your research strategy!

    Returns shortage information including:
    - Current shortage status
    - Shortage start and resolution dates
    - Reason for shortage
    - Therapeutic category
    - Manufacturer information
    - Estimated resolution timeline

    Note: Shortage data is cached and updated periodically.
    Check FDA.gov for most current information.
    

**Input Parameters**:
```json
{
  "properties": {
    "drug": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Drug name (generic or brand) to search",
      "title": "Drug"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Shortage status (current or resolved)",
      "title": "Status"
    },
    "therapeutic_category": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Therapeutic category (e.g., Oncology, Anti-infective)",
      "title": "Therapeutic Category"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "maximum": 100,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based)",
      "minimum": 1,
      "title": "Page",
      "type": "integer"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "title": "openfda_shortage_searcherArguments",
  "type": "object"
}
```

#### openfda_shortage_getter

**Description**: Get detailed FDA drug shortage information for a specific drug.

    Returns comprehensive shortage details including:
    - Complete timeline of shortage
    - Detailed reason for shortage
    - All affected manufacturers
    - Alternative products if available
    - Resolution status and estimates
    - Additional notes and recommendations

    Data is updated periodically from FDA shortage database.
    

**Input Parameters**:
```json
{
  "properties": {
    "drug": {
      "description": "Drug name (generic or brand)",
      "title": "Drug",
      "type": "string"
    },
    "api_key": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional OpenFDA API key (overrides OPENFDA_API_KEY env var)",
      "title": "Api Key"
    }
  },
  "required": [
    "drug"
  ],
  "title": "openfda_shortage_getterArguments",
  "type": "object"
}
```

---

###  Call for Papers

**Description**: 

**Connection Status**: success

**Available Tools** (1 ):

#### get_events

**Description**: Search for conferences matching specific keywords.

**Input Parameters**:
```json
{
  "properties": {
    "keywords": {
      "title": "Keywords",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "keywords"
  ],
  "title": "get_eventsArguments",
  "type": "object"
}
```

---

###  Car Price Evaluator

**Description**: 

**Connection Status**: success

**Available Tools** (3 ):

#### get_car_brands

**Description**: 
    Get all available car brands from FIPE API.
    
    Returns:
        List of car brands with their codes and names
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "get_car_brandsArguments",
  "type": "object"
}
```

#### search_car_price

**Description**: 
    Search for car models and prices by brand name.
    
    Args:
        brand_name: The car brand name to search for (e.g., "Toyota", "Honda", "Ford")
    
    Returns:
        Car models with current market prices from FIPE database
    

**Input Parameters**:
```json
{
  "properties": {
    "brand_name": {
      "title": "Brand Name",
      "type": "string"
    }
  },
  "required": [
    "brand_name"
  ],
  "title": "search_car_priceArguments",
  "type": "object"
}
```

#### get_vehicles_by_type

**Description**: 
    Get vehicles by type (cars, motorcycles, trucks).
    
    Args:
        vehicle_type: Type of vehicles to fetch ("carros"/"cars", "motos"/"motorcycles", "caminhoes"/"trucks")
    
    Returns:
        List of vehicle brands for the specified type
    

**Input Parameters**:
```json
{
  "properties": {
    "vehicle_type": {
      "default": "carros",
      "title": "Vehicle Type",
      "type": "string"
    }
  },
  "title": "get_vehicles_by_typeArguments",
  "type": "object"
}
```

---

###  Context7

**Description**: 

**Connection Status**: success

**Available Tools** (2 ):

#### resolve-library-id

**Description**: Resolves a package/product name to a Context7-compatible library ID and returns a list of matching libraries.

You MUST call this function before 'get-library-docs' to obtain a valid Context7-compatible library ID UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

Selection Process:
1. Analyze the query to understand what library/package the user is looking for
2. Return the most relevant match based on:
- Name similarity to the query (exact matches prioritized)
- Description relevance to the query's intent
- Documentation coverage (prioritize libraries with higher Code Snippet counts)
- Trust score (consider libraries with scores of 7-10 more authoritative)

Response Format:
- Return the selected library ID in a clearly marked section
- Provide a brief explanation for why this library was chosen
- If multiple good matches exist, acknowledge this but proceed with the most relevant one
- If no good matches exist, clearly state this and suggest query refinements

For ambiguous queries, request clarification before proceeding with a best-guess match.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "libraryName": {
      "type": "string",
      "description": "Library name to search for and retrieve a Context7-compatible library ID."
    }
  },
  "required": [
    "libraryName"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### get-library-docs

**Description**: Fetches up-to-date documentation for a library. You must call 'resolve-library-id' first to obtain the exact Context7-compatible library ID required to use this tool, UNLESS the user explicitly provides a library ID in the format '/org/project' or '/org/project/version' in their query.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "context7CompatibleLibraryID": {
      "type": "string",
      "description": "Exact Context7-compatible library ID (e.g., '/mongodb/docs', '/vercel/next.js', '/supabase/supabase', '/vercel/next.js/v14.3.0-canary.87') retrieved from 'resolve-library-id' or directly from user query in the format '/org/project' or '/org/project/version'."
    },
    "topic": {
      "type": "string",
      "description": "Topic to focus documentation on (e.g., 'hooks', 'routing')."
    },
    "tokens": {
      "type": "number",
      "description": "Maximum number of tokens of documentation to retrieve (default: 10000). Higher values provide more context but consume more tokens."
    }
  },
  "required": [
    "context7CompatibleLibraryID"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  DEX Paprika

**Description**: 

**Connection Status**: success

**Available Tools** (11 ):

#### getNetworks

**Description**: REQUIRED FIRST STEP: Get all supported blockchain networks. Always call this first to see available networks before using any network-specific functions. Returns network IDs like "ethereum", "solana", etc.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getNetworkDexes

**Description**: Get available DEXes on a specific network. First call getNetworks to see valid network IDs.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "page": {
      "type": "number",
      "default": 0,
      "description": "Page number for pagination"
    },
    "limit": {
      "type": "number",
      "default": 10,
      "description": "Number of items per page"
    }
  },
  "required": [
    "network"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getNetworkPools

**Description**: PRIMARY POOL FUNCTION: Get top liquidity pools on a specific network. This is the MAIN way to get pool data - there is NO global pools function. Use this instead of any "getTopPools" or "getAllPools" concepts.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (required) - e.g., \"ethereum\", \"solana\""
    },
    "page": {
      "type": "number",
      "default": 0,
      "description": "Page number for pagination"
    },
    "limit": {
      "type": "number",
      "default": 10,
      "description": "Number of items per page (max 100)"
    },
    "sort": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ],
      "default": "desc",
      "description": "Sort order"
    },
    "orderBy": {
      "type": "string",
      "enum": [
        "volume_usd",
        "price_usd",
        "transactions",
        "last_price_change_usd_24h",
        "created_at"
      ],
      "default": "volume_usd",
      "description": "Field to order by"
    }
  },
  "required": [
    "network"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getDexPools

**Description**: Get pools from a specific DEX on a network. First use getNetworks, then getNetworkDexes to find valid DEX IDs.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "dex": {
      "type": "string",
      "description": "DEX identifier from getNetworkDexes (e.g., \"uniswap_v3\")"
    },
    "page": {
      "type": "number",
      "default": 0,
      "description": "Page number for pagination"
    },
    "limit": {
      "type": "number",
      "default": 10,
      "description": "Number of items per page (max 100)"
    },
    "sort": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ],
      "default": "desc",
      "description": "Sort order"
    },
    "orderBy": {
      "type": "string",
      "enum": [
        "volume_usd",
        "price_usd",
        "transactions",
        "last_price_change_usd_24h",
        "created_at"
      ],
      "default": "volume_usd",
      "description": "Field to order by"
    }
  },
  "required": [
    "network",
    "dex"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getPoolDetails

**Description**: Get detailed information about a specific pool. Requires network ID from getNetworks and a pool address.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "poolAddress": {
      "type": "string",
      "description": "Pool address or identifier"
    },
    "inversed": {
      "type": "boolean",
      "default": false,
      "description": "Whether to invert the price ratio"
    }
  },
  "required": [
    "network",
    "poolAddress"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getTokenDetails

**Description**: Get detailed information about a specific token on a network. First use getNetworks to get valid network IDs.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "tokenAddress": {
      "type": "string",
      "description": "Token address or identifier"
    }
  },
  "required": [
    "network",
    "tokenAddress"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getTokenPools

**Description**: Get liquidity pools containing a specific token on a network. Great for finding where a token is traded.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "tokenAddress": {
      "type": "string",
      "description": "Token address or identifier"
    },
    "page": {
      "type": "number",
      "default": 0,
      "description": "Page number for pagination"
    },
    "limit": {
      "type": "number",
      "default": 10,
      "description": "Number of items per page (max 100)"
    },
    "sort": {
      "type": "string",
      "enum": [
        "asc",
        "desc"
      ],
      "default": "desc",
      "description": "Sort order"
    },
    "orderBy": {
      "type": "string",
      "enum": [
        "volume_usd",
        "price_usd",
        "transactions",
        "last_price_change_usd_24h",
        "created_at"
      ],
      "default": "volume_usd",
      "description": "Field to order by"
    },
    "reorder": {
      "type": "boolean",
      "description": "If true, reorders the pool so that the specified token becomes the primary token for all metrics"
    },
    "address": {
      "type": "string",
      "description": "Filter pools that contain this additional token address"
    }
  },
  "required": [
    "network",
    "tokenAddress"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getPoolOHLCV

**Description**: Get historical price data (OHLCV) for a pool - essential for price analysis, backtesting, and visualization. Requires network and pool address.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "poolAddress": {
      "type": "string",
      "description": "Pool address or identifier"
    },
    "start": {
      "type": "string",
      "description": "Start time for historical data (Unix timestamp, RFC3339 timestamp, or yyyy-mm-dd format)"
    },
    "end": {
      "type": "string",
      "description": "End time for historical data (max 1 year from start)"
    },
    "limit": {
      "type": "number",
      "default": 1,
      "description": "Number of data points to retrieve (max 366) - adjust for different analysis needs"
    },
    "interval": {
      "type": "string",
      "default": "24h",
      "description": "Interval granularity: 1m, 5m, 10m, 15m, 30m, 1h, 6h, 12h, 24h"
    },
    "inversed": {
      "type": "boolean",
      "default": false,
      "description": "Whether to invert the price ratio for alternative pair perspective (e.g., ETH/USDC vs USDC/ETH)"
    }
  },
  "required": [
    "network",
    "poolAddress",
    "start"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getPoolTransactions

**Description**: Get recent transactions for a specific pool. Shows swaps, adds, removes. Requires network and pool address.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "network": {
      "type": "string",
      "description": "Network ID from getNetworks (e.g., \"ethereum\", \"solana\")"
    },
    "poolAddress": {
      "type": "string",
      "description": "Pool address or identifier"
    },
    "page": {
      "type": "number",
      "default": 0,
      "description": "Page number for pagination (up to 100 pages)"
    },
    "limit": {
      "type": "number",
      "default": 10,
      "description": "Number of items per page (max 100)"
    },
    "cursor": {
      "type": "string",
      "description": "Transaction ID used for cursor-based pagination"
    }
  },
  "required": [
    "network",
    "poolAddress"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### search

**Description**: Search across ALL networks for tokens, pools, and DEXes by name, symbol, or address. Good starting point when you don't know the specific network.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search term (e.g., \"uniswap\", \"bitcoin\", or a token address)"
    }
  },
  "required": [
    "query"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getStats

**Description**: Get high-level statistics about the DexPaprika ecosystem: total networks, DEXes, pools, and tokens available.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  FruityVice

**Description**: 

**Connection Status**: success

**Available Tools** (1 ):

#### get_fruit_nutrition

**Description**: 
    Get nutritional information and details for a given fruit name.

    Args:
        fruit_name: The name of the fruit to get information about (e.g., "apple", "banana", "orange")

    Returns:
        Dictionary containing fruit information including name, family, genus, order, and nutritional data
    

**Input Parameters**:
```json
{
  "properties": {
    "fruit_name": {
      "title": "Fruit Name",
      "type": "string"
    }
  },
  "required": [
    "fruit_name"
  ],
  "title": "get_fruit_nutritionArguments",
  "type": "object"
}
```

---

###  Game Trends

**Description**: 

**Connection Status**: success

**Available Tools** (7 ):

#### get_steam_trending_games

**Description**: Get real trending games from Steam platform with live data from multiple sources.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_steam_top_sellers

**Description**: Get real top selling games from Steam platform with live sales data.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_steam_most_played

**Description**: Get real-time most played games from Steam with live player statistics from SteamCharts.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_epic_free_games

**Description**: Get current and upcoming free games from Epic Games Store with real promotion data.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_epic_trending_games

**Description**: Get trending games from Epic Games Store.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_all_trending_games

**Description**: Get comprehensive real-time gaming data from all platforms (Steam and Epic Games).

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

#### get_api_health

**Description**: Check the health status of the Gaming Trend Analytics API.

**Input Parameters**:
```json
{
  "properties": {},
  "type": "object"
}
```

---

###  Huge Icons

**Description**: 

**Connection Status**: success

**Available Tools** (3 ):

#### list_icons

**Description**: Get a list of all available Hugeicons icons

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {},
  "required": []
}
```

#### search_icons

**Description**: Search for icons by name or tags. Use commas to search for multiple icons (e.g. 'home, notification, settings')

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search query to find relevant icons. Separate multiple searches with commas"
    }
  },
  "required": [
    "query"
  ]
}
```

#### get_platform_usage

**Description**: Get platform-specific usage instructions for Hugeicons

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "platform": {
      "type": "string",
      "description": "Platform name (react, vue, angular, svelte, react-native, flutter)",
      "enum": [
        "react",
        "vue",
        "angular",
        "svelte",
        "react-native",
        "flutter"
      ]
    }
  },
  "required": [
    "platform"
  ]
}
```

---

###  Hugging Face

**Description**: 

**Connection Status**: success

**Available Tools** (10 ):

#### search-models

**Description**: Search for models on Hugging Face Hub

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search term (e.g., 'bert', 'gpt')"
    },
    "author": {
      "type": "string",
      "description": "Filter by author/organization (e.g., 'huggingface', 'google')"
    },
    "tags": {
      "type": "string",
      "description": "Filter by tags (e.g., 'text-classification', 'translation')"
    },
    "limit": {
      "type": "integer",
      "description": "Maximum number of results to return"
    }
  }
}
```

#### get-model-info

**Description**: Get detailed information about a specific model

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "description": "The ID of the model (e.g., 'google/bert-base-uncased')"
    }
  },
  "required": [
    "model_id"
  ]
}
```

#### search-datasets

**Description**: Search for datasets on Hugging Face Hub

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search term"
    },
    "author": {
      "type": "string",
      "description": "Filter by author/organization"
    },
    "tags": {
      "type": "string",
      "description": "Filter by tags"
    },
    "limit": {
      "type": "integer",
      "description": "Maximum number of results to return"
    }
  }
}
```

#### get-dataset-info

**Description**: Get detailed information about a specific dataset

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "dataset_id": {
      "type": "string",
      "description": "The ID of the dataset (e.g., 'squad')"
    }
  },
  "required": [
    "dataset_id"
  ]
}
```

#### search-spaces

**Description**: Search for Spaces on Hugging Face Hub

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search term"
    },
    "author": {
      "type": "string",
      "description": "Filter by author/organization"
    },
    "tags": {
      "type": "string",
      "description": "Filter by tags"
    },
    "sdk": {
      "type": "string",
      "description": "Filter by SDK (e.g., 'streamlit', 'gradio', 'docker')"
    },
    "limit": {
      "type": "integer",
      "description": "Maximum number of results to return"
    }
  }
}
```

#### get-space-info

**Description**: Get detailed information about a specific Space

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "space_id": {
      "type": "string",
      "description": "The ID of the Space (e.g., 'huggingface/diffusers-demo')"
    }
  },
  "required": [
    "space_id"
  ]
}
```

#### get-paper-info

**Description**: Get information about a specific paper on Hugging Face

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "arxiv_id": {
      "type": "string",
      "description": "The arXiv ID of the paper (e.g., '1810.04805')"
    }
  },
  "required": [
    "arxiv_id"
  ]
}
```

#### get-daily-papers

**Description**: Get the list of daily papers curated by Hugging Face

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {}
}
```

#### search-collections

**Description**: Search for collections on Hugging Face Hub

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "owner": {
      "type": "string",
      "description": "Filter by owner"
    },
    "item": {
      "type": "string",
      "description": "Filter by item (e.g., 'models/teknium/OpenHermes-2.5-Mistral-7B')"
    },
    "query": {
      "type": "string",
      "description": "Search term for titles and descriptions"
    },
    "limit": {
      "type": "integer",
      "description": "Maximum number of results to return"
    }
  }
}
```

#### get-collection-info

**Description**: Get detailed information about a specific collection

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "description": "The namespace of the collection (user or organization)"
    },
    "collection_id": {
      "type": "string",
      "description": "The ID part of the collection"
    }
  },
  "required": [
    "namespace",
    "collection_id"
  ]
}
```

---

###  Math MCP

**Description**: 

**Connection Status**: success

**Available Tools** (13 ):

#### add

**Description**: Adds two numbers together

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "firstNumber": {
      "type": "number",
      "description": "The first addend"
    },
    "secondNumber": {
      "type": "number",
      "description": "The second addend"
    }
  },
  "required": [
    "firstNumber",
    "secondNumber"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### subtract

**Description**: Subtracts the second number from the first number

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "minuend": {
      "type": "number",
      "description": "The number to subtract from (minuend)"
    },
    "subtrahend": {
      "type": "number",
      "description": "The number being subtracted (subtrahend)"
    }
  },
  "required": [
    "minuend",
    "subtrahend"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### multiply

**Description**: Multiplies two numbers together

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "firstNumber": {
      "type": "number",
      "description": "The first number"
    },
    "SecondNumber": {
      "type": "number",
      "description": "The second number"
    }
  },
  "required": [
    "firstNumber",
    "SecondNumber"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### division

**Description**: Divides the first number by the second number

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numerator": {
      "type": "number",
      "description": "The number being divided (numerator)"
    },
    "denominator": {
      "type": "number",
      "description": "The number to divide by (denominator)"
    }
  },
  "required": [
    "numerator",
    "denominator"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### sum

**Description**: Adds any number of numbers together

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "minItems": 1,
      "description": "Array of numbers to sum"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### mean

**Description**: Calculates the arithmetic mean of a list of numbers

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "minItems": 1,
      "description": "Array of numbers to find the mean of"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### median

**Description**: Calculates the median of a list of numbers

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "minItems": 1,
      "description": "Array of numbers to find the median of"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### mode

**Description**: Finds the most common number in a list of numbers

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "Array of numbers to find the mode of"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### min

**Description**: Finds the minimum value from a list of numbers

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "Array of numbers to find the minimum of"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### max

**Description**: Finds the maximum value from a list of numbers

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "numbers": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "Array of numbers to find the maximum of"
    }
  },
  "required": [
    "numbers"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### floor

**Description**: Rounds a number down to the nearest integer

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "number": {
      "type": "number",
      "description": "The number to round down"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### ceiling

**Description**: Rounds a number up to the nearest integer

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "number": {
      "type": "number",
      "description": "The number to round up"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### round

**Description**: Rounds a number to the nearest integer

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "number": {
      "type": "number",
      "description": "The number to round"
    }
  },
  "required": [
    "number"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  NixOS

**Description**: 

**Connection Status**: success

**Available Tools** (18 ):

#### nixos_search

**Description**: Search NixOS packages, options, or programs.

    Args:
        query: Search term to look for
        search_type: Type of search - "packages", "options", "programs", or "flakes"
        limit: Maximum number of results to return (1-100)
        channel: NixOS channel to search in (e.g., "unstable", "stable", "25.05")

    Returns:
        Plain text results with bullet points or error message
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "search_type": {
      "default": "packages",
      "title": "Search Type",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    },
    "channel": {
      "default": "unstable",
      "title": "Channel",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "nixos_searchArguments",
  "type": "object"
}
```

#### nixos_info

**Description**: Get detailed info about a NixOS package or option.

    Args:
        name: Name of the package or option to look up
        type: Type of lookup - "package" or "option"
        channel: NixOS channel to search in (e.g., "unstable", "stable", "25.05")

    Returns:
        Plain text details about the package/option or error message
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "type": {
      "default": "package",
      "title": "Type",
      "type": "string"
    },
    "channel": {
      "default": "unstable",
      "title": "Channel",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "nixos_infoArguments",
  "type": "object"
}
```

#### nixos_channels

**Description**: List available NixOS channels with their status.

    Returns:
        Plain text list showing channel names, versions, and availability
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "nixos_channelsArguments",
  "type": "object"
}
```

#### nixos_stats

**Description**: Get NixOS statistics for a channel.

    Args:
        channel: NixOS channel to get stats for (e.g., "unstable", "stable", "25.05")

    Returns:
        Plain text statistics including package/option counts
    

**Input Parameters**:
```json
{
  "properties": {
    "channel": {
      "default": "unstable",
      "title": "Channel",
      "type": "string"
    }
  },
  "title": "nixos_statsArguments",
  "type": "object"
}
```

#### home_manager_search

**Description**: Search Home Manager configuration options.

    Searches through available Home Manager options by name and description.

    Args:
        query: The search query string to match against option names and descriptions
        limit: Maximum number of results to return (default: 20, max: 100)

    Returns:
        Plain text list of matching options with name, type, and description
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "home_manager_searchArguments",
  "type": "object"
}
```

#### home_manager_info

**Description**: Get detailed information about a specific Home Manager option.

    Requires an exact option name match. If not found, suggests similar options.

    Args:
        name: The exact option name (e.g., 'programs.git.enable')

    Returns:
        Plain text with option details (name, type, description) or error with suggestions
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "home_manager_infoArguments",
  "type": "object"
}
```

#### home_manager_stats

**Description**: Get statistics about Home Manager options.

    Retrieves overall statistics including total options, categories, and top categories.

    Returns:
        Plain text summary with total options, category count, and top 5 categories
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "home_manager_statsArguments",
  "type": "object"
}
```

#### home_manager_list_options

**Description**: List all Home Manager option categories.

    Enumerates all top-level categories with their option counts.

    Returns:
        Plain text list of categories sorted alphabetically with option counts
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "home_manager_list_optionsArguments",
  "type": "object"
}
```

#### home_manager_options_by_prefix

**Description**: Get Home Manager options matching a specific prefix.

    Useful for browsing options under a category or finding exact option names.

    Args:
        option_prefix: The prefix to match (e.g., 'programs.git' or 'services')

    Returns:
        Plain text list of options with the given prefix, including descriptions
    

**Input Parameters**:
```json
{
  "properties": {
    "option_prefix": {
      "title": "Option Prefix",
      "type": "string"
    }
  },
  "required": [
    "option_prefix"
  ],
  "title": "home_manager_options_by_prefixArguments",
  "type": "object"
}
```

#### darwin_search

**Description**: Search nix-darwin (macOS) configuration options.

    Searches through available nix-darwin options by name and description.

    Args:
        query: The search query string to match against option names and descriptions
        limit: Maximum number of results to return (default: 20, max: 100)

    Returns:
        Plain text list of matching options with name, type, and description
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "darwin_searchArguments",
  "type": "object"
}
```

#### darwin_info

**Description**: Get detailed information about a specific nix-darwin option.

    Requires an exact option name match. If not found, suggests similar options.

    Args:
        name: The exact option name (e.g., 'system.defaults.dock.autohide')

    Returns:
        Plain text with option details (name, type, description) or error with suggestions
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "darwin_infoArguments",
  "type": "object"
}
```

#### darwin_stats

**Description**: Get statistics about nix-darwin options.

    Retrieves overall statistics including total options, categories, and top categories.

    Returns:
        Plain text summary with total options, category count, and top 5 categories
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "darwin_statsArguments",
  "type": "object"
}
```

#### darwin_list_options

**Description**: List all nix-darwin option categories.

    Enumerates all top-level categories with their option counts.

    Returns:
        Plain text list of categories sorted alphabetically with option counts
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "darwin_list_optionsArguments",
  "type": "object"
}
```

#### darwin_options_by_prefix

**Description**: Get nix-darwin options matching a specific prefix.

    Useful for browsing options under a category or finding exact option names.

    Args:
        option_prefix: The prefix to match (e.g., 'system.defaults' or 'services')

    Returns:
        Plain text list of options with the given prefix, including descriptions
    

**Input Parameters**:
```json
{
  "properties": {
    "option_prefix": {
      "title": "Option Prefix",
      "type": "string"
    }
  },
  "required": [
    "option_prefix"
  ],
  "title": "darwin_options_by_prefixArguments",
  "type": "object"
}
```

#### nixos_flakes_stats

**Description**: Get statistics about available NixOS flakes.

    Retrieves statistics from the flake search index including total packages,
    unique repositories, flake types, and top contributors.

    Returns:
        Plain text summary with flake statistics and top contributors
    

**Input Parameters**:
```json
{
  "properties": {},
  "title": "nixos_flakes_statsArguments",
  "type": "object"
}
```

#### nixos_flakes_search

**Description**: Search NixOS flakes by name, description, owner, or repository.

    Searches the flake index for community-contributed packages and configurations.
    Flakes are indexed separately from official packages.

    Args:
        query: The search query (flake name, description, owner, or repository)
        limit: Maximum number of results to return (default: 20, max: 100)
        channel: Ignored - flakes use a separate indexing system

    Returns:
        Plain text list of unique flakes with their packages and metadata
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    },
    "channel": {
      "default": "unstable",
      "title": "Channel",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "nixos_flakes_searchArguments",
  "type": "object"
}
```

#### nixhub_package_versions

**Description**: Get version history and nixpkgs commit hashes for a specific package from NixHub.io.

    Use this tool when users need specific package versions or commit hashes for reproducible builds.

    Args:
        package_name: Name of the package to query (e.g., "firefox", "python")
        limit: Maximum number of versions to return (default: 10, max: 50)

    Returns:
        Plain text with package info and version history including commit hashes
    

**Input Parameters**:
```json
{
  "properties": {
    "package_name": {
      "title": "Package Name",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "package_name"
  ],
  "title": "nixhub_package_versionsArguments",
  "type": "object"
}
```

#### nixhub_find_version

**Description**: Find a specific version of a package in NixHub with smart search.

    Automatically searches with increasing limits to find the requested version.

    Args:
        package_name: Name of the package to query (e.g., "ruby", "python")
        version: Specific version to find (e.g., "2.6.7", "3.5.9")

    Returns:
        Plain text with version info and commit hash if found, or helpful message if not
    

**Input Parameters**:
```json
{
  "properties": {
    "package_name": {
      "title": "Package Name",
      "type": "string"
    },
    "version": {
      "title": "Version",
      "type": "string"
    }
  },
  "required": [
    "package_name",
    "version"
  ],
  "title": "nixhub_find_versionArguments",
  "type": "object"
}
```

---

###  OSINT Intelligence

**Description**: 

**Connection Status**: success

**Available Tools** (7 ):

#### whois_lookup

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

#### nmap_scan

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

#### dnsrecon_lookup

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

#### dnstwist_lookup

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "domain": {
      "type": "string"
    }
  },
  "required": [
    "domain"
  ],
  "type": "object"
}
```

#### dig_lookup

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

#### host_lookup

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

#### osint_overview

**Description**: 

**Input Parameters**:
```json
{
  "properties": {
    "target": {
      "type": "string"
    }
  },
  "required": [
    "target"
  ],
  "type": "object"
}
```

---

###  Reddit

**Description**: 

**Connection Status**: success_no_tools

**Available Tools**: None

---

###  National Parks

**Description**: 

**Connection Status**: success

**Available Tools** (6 ):

#### findParks

**Description**: Search for national parks based on state, name, activities, or other criteria

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "stateCode": {
      "type": "string",
      "description": "Filter parks by state code (e.g., \"CA\" for California, \"NY\" for New York). Multiple states can be comma-separated (e.g., \"CA,OR,WA\")"
    },
    "q": {
      "type": "string",
      "description": "Search term to filter parks by name or description"
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of parks to return (default: 10, max: 50)"
    },
    "start": {
      "type": "number",
      "description": "Start position for results (useful for pagination)"
    },
    "activities": {
      "type": "string",
      "description": "Filter by available activities (e.g., \"hiking,camping\")"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getParkDetails

**Description**: Get detailed information about a specific national park

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "parkCode": {
      "type": "string",
      "description": "The park code of the national park (e.g., \"yose\" for Yosemite, \"grca\" for Grand Canyon)"
    }
  },
  "required": [
    "parkCode"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getAlerts

**Description**: Get current alerts for national parks including closures, hazards, and important information

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "parkCode": {
      "type": "string",
      "description": "Filter alerts by park code (e.g., \"yose\" for Yosemite). Multiple parks can be comma-separated (e.g., \"yose,grca\")."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of alerts to return (default: 10, max: 50)"
    },
    "start": {
      "type": "number",
      "description": "Start position for results (useful for pagination)"
    },
    "q": {
      "type": "string",
      "description": "Search term to filter alerts by title or description"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getVisitorCenters

**Description**: Get information about visitor centers and their operating hours

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "parkCode": {
      "type": "string",
      "description": "Filter visitor centers by park code (e.g., \"yose\" for Yosemite). Multiple parks can be comma-separated (e.g., \"yose,grca\")."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of visitor centers to return (default: 10, max: 50)"
    },
    "start": {
      "type": "number",
      "description": "Start position for results (useful for pagination)"
    },
    "q": {
      "type": "string",
      "description": "Search term to filter visitor centers by name or description"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getCampgrounds

**Description**: Get information about available campgrounds and their amenities

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "parkCode": {
      "type": "string",
      "description": "Filter campgrounds by park code (e.g., \"yose\" for Yosemite). Multiple parks can be comma-separated (e.g., \"yose,grca\")."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of campgrounds to return (default: 10, max: 50)"
    },
    "start": {
      "type": "number",
      "description": "Start position for results (useful for pagination)"
    },
    "q": {
      "type": "string",
      "description": "Search term to filter campgrounds by name or description"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### getEvents

**Description**: Find upcoming events at parks

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "parkCode": {
      "type": "string",
      "description": "Filter events by park code (e.g., \"yose\" for Yosemite). Multiple parks can be comma-separated (e.g., \"yose,grca\")."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of events to return (default: 10, max: 50)"
    },
    "start": {
      "type": "number",
      "description": "Start position for results (useful for pagination)"
    },
    "dateStart": {
      "type": "string",
      "description": "Start date for filtering events (format: YYYY-MM-DD)"
    },
    "dateEnd": {
      "type": "string",
      "description": "End date for filtering events (format: YYYY-MM-DD)"
    },
    "q": {
      "type": "string",
      "description": "Search term to filter events by title or description"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  Medical Calculator

**Description**: 

**Connection Status**: success

**Available Tools** (22 ):

#### egfr_epi

**Description**: 
    Estimated Glomerular Filtration Rate (eGFR) using the EPI formula (version 2021)
    Reference: N Engl J Med. 2021 Nov 4;385(19):1737-1749
    
    Parameters:
    -----------
    scr : float
        serum creatinine level in mg/dL
    age : int
        Age in years
    male : bool
        true if Male
    
    Returns:
    --------
    float
        Estimated GFR in mL/min/1.73m^2
    

**Input Parameters**:
```json
{
  "properties": {
    "scr": {
      "title": "Scr",
      "type": "number"
    },
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "male": {
      "title": "Male",
      "type": "boolean"
    }
  },
  "required": [
    "scr",
    "age",
    "male"
  ],
  "title": "egfr_epiArguments",
  "type": "object"
}
```

#### egfr_epi_cr_cys

**Description**: 
    Estimated Glomerular Filtration Rate (eGFR) using the 2021 CKD-EPI Creatinine-Cystatin C equation
    Reference: N Engl J Med. 2021 Nov 4;385(19):1737-1749
    
    Parameters:
    -----------
    scr : float
        Serum creatinine level in mg/dL
    scys : float
        Serum cystatin C level in mg/L
    age : int
        Age in years
    male : bool
        True if patient is male, False if female
    
    Returns:
    --------
    dict
        Dictionary containing eGFR result and calculation parameters
    

**Input Parameters**:
```json
{
  "properties": {
    "scr": {
      "title": "Scr",
      "type": "number"
    },
    "scys": {
      "title": "Scys",
      "type": "number"
    },
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "male": {
      "title": "Male",
      "type": "boolean"
    }
  },
  "required": [
    "scr",
    "scys",
    "age",
    "male"
  ],
  "title": "egfr_epi_cr_cysArguments",
  "type": "object"
}
```

#### bp_children

**Description**: 
    혈압 센타일(percentile)을 계산하는 함수
    
    Parameters:
    -----------
    years : int
        나이(년)
    months : int
        나이(월)
    height : int
        키(cm)
    sex : str
        성별 ('male' 또는 'female')
    systolic : int
        수축기 혈압(mmHg)
    diastolic : int
        이완기 혈압(mmHg)
    
    Returns:
    --------
    dict
        수축기 및 이완기 혈압 센타일 결과를 포함하는 딕셔너리
    

**Input Parameters**:
```json
{
  "properties": {
    "years": {
      "title": "Years",
      "type": "integer"
    },
    "months": {
      "title": "Months",
      "type": "integer"
    },
    "height": {
      "title": "Height",
      "type": "integer"
    },
    "sex": {
      "title": "Sex",
      "type": "string"
    },
    "systolic": {
      "title": "Systolic",
      "type": "integer"
    },
    "diastolic": {
      "title": "Diastolic",
      "type": "integer"
    }
  },
  "required": [
    "years",
    "months",
    "height",
    "sex",
    "systolic",
    "diastolic"
  ],
  "title": "bp_childrenArguments",
  "type": "object"
}
```

#### bmi_bsa_calculator

**Description**: 
    Calculates Body Mass Index (BMI) and Body Surface Area (BSA)
    
    Parameters:
    -----------
    weight : float
        Weight in kilograms
    height : float
        Height in centimeters (default) or meters
    height_unit : str
        Unit of height measurement ('cm' or 'm', default is 'cm')
    
    Returns:
    --------
    dict
        Dictionary containing BMI, BSA, and classification
    

**Input Parameters**:
```json
{
  "properties": {
    "weight": {
      "title": "Weight",
      "type": "number"
    },
    "height": {
      "title": "Height",
      "type": "number"
    },
    "height_unit": {
      "default": "cm",
      "title": "Height Unit",
      "type": "string"
    }
  },
  "required": [
    "weight",
    "height"
  ],
  "title": "bmi_bsa_calculatorArguments",
  "type": "object"
}
```

#### crcl_cockcroft_gault

**Description**: 
    Calculate Creatinine Clearance using the Cockcroft-Gault formula
    
    Parameters:
    -----------
    age : int
        Age in years
    weight : float
        Actual body weight in kg
    height : float
        Height in inches
    scr : float
        Serum creatinine in mg/dL
    sex : str
        Gender ('male' or 'female')
    
    Returns:
    --------
    dict
        Dictionary containing creatinine clearance result and weight calculations
    

**Input Parameters**:
```json
{
  "properties": {
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "weight": {
      "title": "Weight",
      "type": "number"
    },
    "height": {
      "title": "Height",
      "type": "number"
    },
    "scr": {
      "title": "Scr",
      "type": "number"
    },
    "sex": {
      "title": "Sex",
      "type": "string"
    }
  },
  "required": [
    "age",
    "weight",
    "height",
    "scr",
    "sex"
  ],
  "title": "crcl_cockcroft_gaultArguments",
  "type": "object"
}
```

#### map_calculator

**Description**: 
    Calculate Mean Arterial Pressure (MAP)
    
    Parameters:
    -----------
    sbp : int
        Systolic Blood Pressure in mmHg
    dbp : int
        Diastolic Blood Pressure in mmHg
    
    Returns:
    --------
    dict
        Dictionary containing MAP result and input values
    

**Input Parameters**:
```json
{
  "properties": {
    "sbp": {
      "title": "Sbp",
      "type": "integer"
    },
    "dbp": {
      "title": "Dbp",
      "type": "integer"
    }
  },
  "required": [
    "sbp",
    "dbp"
  ],
  "title": "map_calculatorArguments",
  "type": "object"
}
```

#### chads2_vasc_score

**Description**: 
    Calculate CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk
    
    Parameters:
    -----------
    age : int
        Age in years
    female : bool
        True if patient is female, False if male
    chf : bool
        True if patient has history of congestive heart failure
    hypertension : bool
        True if patient has history of hypertension
    stroke_history : bool
        True if patient has history of stroke, TIA, or thromboembolism
    vascular_disease : bool
        True if patient has history of vascular disease (prior MI, peripheral artery disease, or aortic plaque)
    diabetes : bool
        True if patient has history of diabetes mellitus
    
    Returns:
    --------
    dict
        Dictionary containing CHA₂DS₂-VASc score and risk factors
    

**Input Parameters**:
```json
{
  "properties": {
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "female": {
      "title": "Female",
      "type": "boolean"
    },
    "chf": {
      "title": "Chf",
      "type": "boolean"
    },
    "hypertension": {
      "title": "Hypertension",
      "type": "boolean"
    },
    "stroke_history": {
      "title": "Stroke History",
      "type": "boolean"
    },
    "vascular_disease": {
      "title": "Vascular Disease",
      "type": "boolean"
    },
    "diabetes": {
      "title": "Diabetes",
      "type": "boolean"
    }
  },
  "required": [
    "age",
    "female",
    "chf",
    "hypertension",
    "stroke_history",
    "vascular_disease",
    "diabetes"
  ],
  "title": "chads2_vasc_scoreArguments",
  "type": "object"
}
```

#### prevent_cvd_risk

**Description**: 
    Predicting Risk of Cardiovascular Disease EVENTs (PREVENT)
    Predicts 10-year risk of CVD in patients aged 30-79 without known CVD.
    
    Parameters:
    -----------
    age : int
        Age in years (30-79)
    female : bool
        True if patient is female, False if male
    tc : float
        Total cholesterol in mmol/L
    hdl : float
        HDL cholesterol in mmol/L
    sbp : int
        Systolic blood pressure in mmHg
    diabetes : bool
        True if patient has diabetes
    current_smoker : bool
        True if patient is a current smoker
    egfr : float
        Estimated glomerular filtration rate in mL/min/1.73m²
    using_antihtn : bool
        True if patient is using antihypertensive drugs
    using_statins : bool
        True if patient is using statins
    
    Returns:
    --------
    dict
        Dictionary containing 10-year CVD risk and calculation details
    

**Input Parameters**:
```json
{
  "properties": {
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "female": {
      "title": "Female",
      "type": "boolean"
    },
    "tc": {
      "title": "Tc",
      "type": "number"
    },
    "hdl": {
      "title": "Hdl",
      "type": "number"
    },
    "sbp": {
      "title": "Sbp",
      "type": "integer"
    },
    "diabetes": {
      "title": "Diabetes",
      "type": "boolean"
    },
    "current_smoker": {
      "title": "Current Smoker",
      "type": "boolean"
    },
    "egfr": {
      "title": "Egfr",
      "type": "number"
    },
    "using_antihtn": {
      "title": "Using Antihtn",
      "type": "boolean"
    },
    "using_statins": {
      "title": "Using Statins",
      "type": "boolean"
    }
  },
  "required": [
    "age",
    "female",
    "tc",
    "hdl",
    "sbp",
    "diabetes",
    "current_smoker",
    "egfr",
    "using_antihtn",
    "using_statins"
  ],
  "title": "prevent_cvd_riskArguments",
  "type": "object"
}
```

#### corrected_calcium

**Description**: 
    Calcium Correction for Hypoalbuminemia and Hyperalbuminemia
    Calculates a corrected calcium level for patients with abnormal albumin levels.
    
    Parameters:
    -----------
    serum_calcium : float
        Patient's measured serum calcium level in mg/dL
    patient_albumin : float
        Patient's serum albumin level in g/dL
    normal_albumin : float, optional
        Normal/reference albumin level in g/dL, default is 4.0 g/dL
    
    Returns:
    --------
    dict
        Dictionary containing corrected calcium value, interpretation, and calculation details
        
    Formula:
    --------
    Corrected Calcium = (0.8 * (Normal Albumin - Patient's Albumin)) + Serum Calcium
    
    References:
    -----------
    Payne RB, et al. Br Med J. 1973;4(5893):643-646.
    

**Input Parameters**:
```json
{
  "properties": {
    "serum_calcium": {
      "title": "Serum Calcium",
      "type": "number"
    },
    "patient_albumin": {
      "title": "Patient Albumin",
      "type": "number"
    },
    "normal_albumin": {
      "default": 4.0,
      "title": "Normal Albumin",
      "type": "number"
    }
  },
  "required": [
    "serum_calcium",
    "patient_albumin"
  ],
  "title": "corrected_calciumArguments",
  "type": "object"
}
```

#### qtc_calculator

**Description**: 
    Corrected QT Interval (QTc) Calculator
    Corrects the QT interval for heart rate extremes using various formulas.
    
    Parameters:
    -----------
    qt_interval : float
        Measured QT interval in milliseconds (ms)
    heart_rate : float
        Heart rate in beats per minute (bpm)
    formula : str, optional
        Formula to use for correction (default: "bazett")
        Options: "bazett", "fridericia", "framingham", "hodges", "rautaharju"
    
    Returns:
    --------
    dict
        Dictionary containing QTc value, interpretation, and calculation details
        
    Formulas:
    ---------
    RR interval = 60 / heart_rate (in seconds)
    Bazett: QTc = QT / √(RR)
    Fridericia: QTc = QT / (RR)^(1/3)
    Framingham: QTc = QT + 154 × (1 - RR)
    Hodges: QTc = QT + 1.75 × (heart_rate - 60)
    Rautaharju: QTc = QT × (120 + heart_rate) / 180
    
    References:
    -----------
    Bazett HC. Heart. 1920;7:353-370
    Fridericia LS. Acta Med Scand. 1920;53:469-486
    Sagie A, et al. Am J Cardiol. 1992;70(7):797-801 (Framingham)
    Hodges M, et al. J Electrocardiol. 1983;16(1):17-24
    Rautaharju PM, et al. J Am Coll Cardiol. 2004;44(3):594-600
    

**Input Parameters**:
```json
{
  "properties": {
    "qt_interval": {
      "title": "Qt Interval",
      "type": "number"
    },
    "heart_rate": {
      "title": "Heart Rate",
      "type": "number"
    },
    "formula": {
      "default": "bazett",
      "title": "Formula",
      "type": "string"
    }
  },
  "required": [
    "qt_interval",
    "heart_rate"
  ],
  "title": "qtc_calculatorArguments",
  "type": "object"
}
```

#### wells_pe_criteria

**Description**: 
    Wells' Criteria for Pulmonary Embolism
    Objectifies risk of pulmonary embolism based on clinical criteria.
    Reference: Wells PS, et al. Thromb Haemost. 2000;83(3):416-20.
    
    Parameters:
    -----------
    clinical_signs_dvt: bool
        Clinical signs and symptoms of DVT (leg swelling, pain with palpation)
    alternative_diagnosis_less_likely: bool
        Alternative diagnosis less likely than PE
    heart_rate_over_100: bool
        Heart rate > 100 beats per minute
    immobilization_or_surgery: bool
        Immobilization or surgery in the previous four weeks
    previous_dvt_or_pe: bool
        Previous DVT/PE
    hemoptysis: bool
        Hemoptysis
    malignancy: bool
        Malignancy (treatment ongoing, treated in last 6 months, or palliative)
    
    Returns:
    --------
    dict
        Dictionary containing the score, risk category for both three-tier and 
        two-tier models, and recommendations
    

**Input Parameters**:
```json
{
  "properties": {
    "clinical_signs_dvt": {
      "default": false,
      "title": "Clinical Signs Dvt",
      "type": "boolean"
    },
    "alternative_diagnosis_less_likely": {
      "default": false,
      "title": "Alternative Diagnosis Less Likely",
      "type": "boolean"
    },
    "heart_rate_over_100": {
      "default": false,
      "title": "Heart Rate Over 100",
      "type": "boolean"
    },
    "immobilization_or_surgery": {
      "default": false,
      "title": "Immobilization Or Surgery",
      "type": "boolean"
    },
    "previous_dvt_or_pe": {
      "default": false,
      "title": "Previous Dvt Or Pe",
      "type": "boolean"
    },
    "hemoptysis": {
      "default": false,
      "title": "Hemoptysis",
      "type": "boolean"
    },
    "malignancy": {
      "default": false,
      "title": "Malignancy",
      "type": "boolean"
    }
  },
  "title": "wells_pe_criteriaArguments",
  "type": "object"
}
```

#### ibw_abw_calculator

**Description**: 
    Ideal Body Weight and Adjusted Body Weight Calculator
    Calculates ideal body weight (Devine formula) and adjusted body weight.
    
    Parameters:
    -----------
    weight_kg : float
        Actual body weight in kilograms
    height_inches : float
        Height in inches
    male : bool
        True if patient is male, False if female
    
    Returns:
    --------
    dict
        Dictionary containing ideal body weight, adjusted body weight, and calculation details
        
    Formulas:
    ---------
    Ideal Body Weight (IBW) (Devine formula):
    - Men: IBW = 50 kg + 2.3 kg × (height in inches - 60)
    - Women: IBW = 45.5 kg + 2.3 kg × (height in inches - 60)
    
    Adjusted Body Weight (ABW):
    - ABW = IBW + 0.4 × (actual weight - IBW)
    
    References:
    -----------
    Devine BJ. Gentamicin therapy. Drug Intell Clin Pharm. 1974;8:650-655.
    Pai MP. Drug Dosing Based on Weight and Body Surface Area: Mathematical Assumptions and Limitations in Obese Adults. Pharmacotherapy. 2012;32(9):856-868.
    

**Input Parameters**:
```json
{
  "properties": {
    "weight_kg": {
      "title": "Weight Kg",
      "type": "number"
    },
    "height_inches": {
      "title": "Height Inches",
      "type": "number"
    },
    "male": {
      "title": "Male",
      "type": "boolean"
    }
  },
  "required": [
    "weight_kg",
    "height_inches",
    "male"
  ],
  "title": "ibw_abw_calculatorArguments",
  "type": "object"
}
```

#### pregnancy_calculator

**Description**: 
    Pregnancy Due Dates Calculator
    Calculates pregnancy dates from last period, gestational age, or date of conception.
    
    Parameters:
    -----------
    calculation_method : str
        Method used for calculation: "lmp" (last menstrual period), "conception", or "ultrasound"
    date_value : str
        Date in format 'YYYY-MM-DD' (date of LMP, conception, or ultrasound)
    cycle_length : int, optional
        Length of menstrual cycle in days (default: 28)
    gestational_age_weeks : int, optional
        Weeks of gestational age at ultrasound (required if calculation_method is "ultrasound")
    gestational_age_days : int, optional
        Days of gestational age at ultrasound (required if calculation_method is "ultrasound")
    
    Returns:
    --------
    dict
        Dictionary containing calculated pregnancy dates and information
        
    Formulas:
    ---------
    - EGA (Estimated Gestational Age) = time since 1st day of LMP
    - EDC (Estimated Date of Conception) = LMP + 2 weeks (adjusted for cycle length)
    - EDD (Estimated Due Date) = LMP + 40 weeks (adjusted for cycle length)
    
    For non-28 day cycles:
    - Adjustment = (cycle_length - 28) days
    - EDD = LMP + 40 weeks + Adjustment
    

**Input Parameters**:
```json
{
  "properties": {
    "calculation_method": {
      "title": "Calculation Method",
      "type": "string"
    },
    "date_value": {
      "title": "Date Value",
      "type": "string"
    },
    "cycle_length": {
      "default": 28,
      "title": "Cycle Length",
      "type": "integer"
    },
    "gestational_age_weeks": {
      "default": null,
      "title": "Gestational Age Weeks",
      "type": "integer"
    },
    "gestational_age_days": {
      "default": null,
      "title": "Gestational Age Days",
      "type": "integer"
    }
  },
  "required": [
    "calculation_method",
    "date_value"
  ],
  "title": "pregnancy_calculatorArguments",
  "type": "object"
}
```

#### revised_cardiac_risk_index

**Description**: 
    Revised Cardiac Risk Index for Pre-Operative Risk
    Estimates risk of cardiac complications after noncardiac surgery.
    
    Parameters:
    -----------
    high_risk_surgery : bool
        Intraperitoneal, intrathoracic, or suprainguinal vascular surgery
    ischemic_heart_disease : bool
        History of MI, positive exercise test, current chest pain considered due to myocardial 
        ischemia, use of nitrate therapy, or ECG with pathological Q waves
    congestive_heart_failure : bool
        Pulmonary edema, bilateral rales, S3 gallop, paroxysmal nocturnal dyspnea, or 
        CXR showing pulmonary vascular redistribution
    cerebrovascular_disease : bool
        Prior transient ischemic attack (TIA) or stroke
    insulin_treatment : bool
        Pre-operative treatment with insulin
    creatinine_over_2mg : bool
        Pre-operative creatinine >2 mg/dL (176.8 µmol/L)
    
    Returns:
    --------
    dict
        Dictionary containing RCRI score and risk interpretation
        
    References:
    -----------
    Lee TH, et al. Circulation. 1999;100(10):1043-1049.
    Canadian Cardiovascular Society (CCS) Guidelines, 2017.
    European Society of Cardiology (ESC) Guidelines, 2022.
    

**Input Parameters**:
```json
{
  "properties": {
    "high_risk_surgery": {
      "default": false,
      "title": "High Risk Surgery",
      "type": "boolean"
    },
    "ischemic_heart_disease": {
      "default": false,
      "title": "Ischemic Heart Disease",
      "type": "boolean"
    },
    "congestive_heart_failure": {
      "default": false,
      "title": "Congestive Heart Failure",
      "type": "boolean"
    },
    "cerebrovascular_disease": {
      "default": false,
      "title": "Cerebrovascular Disease",
      "type": "boolean"
    },
    "insulin_treatment": {
      "default": false,
      "title": "Insulin Treatment",
      "type": "boolean"
    },
    "creatinine_over_2mg": {
      "default": false,
      "title": "Creatinine Over 2Mg",
      "type": "boolean"
    }
  },
  "title": "revised_cardiac_risk_indexArguments",
  "type": "object"
}
```

#### child_pugh_score

**Description**: 
    Calculates the Child-Pugh Score for cirrhosis mortality assessment.

    Parameters:
    -----------
    bilirubin : float
        Total bilirubin in mg/dL.
    albumin : float
        Albumin in g/dL.
    inr : float
        International Normalized Ratio (INR) for prothrombin time.
    ascites : str
        One of: "absent", "slight", "moderate".
    encephalopathy_grade : int
        Hepatic encephalopathy grade: 0 (none), 1-2 (mild), 3-4 (severe).

    Returns:
    --------
    int
        Total Child-Pugh score (5–15).
    

**Input Parameters**:
```json
{
  "properties": {
    "bilirubin": {
      "title": "Bilirubin",
      "type": "number"
    },
    "albumin": {
      "title": "Albumin",
      "type": "number"
    },
    "inr": {
      "title": "Inr",
      "type": "number"
    },
    "ascites": {
      "title": "Ascites",
      "type": "string"
    },
    "encephalopathy_grade": {
      "title": "Encephalopathy Grade",
      "type": "integer"
    }
  },
  "required": [
    "bilirubin",
    "albumin",
    "inr",
    "ascites",
    "encephalopathy_grade"
  ],
  "title": "child_pugh_scoreArguments",
  "type": "object"
}
```

#### steroid_conversion

**Description**: 
    Converts corticosteroid dosages using standard equivalencies.

    Parameters:
    -----------
    from_steroid : str
        Name of the original steroid (e.g., 'prednisone', 'dexamethasone').
    from_dose_mg : float
        Dose of the original steroid in mg.
    to_steroid : str
        Name of the steroid to convert to.

    Returns:
    --------
    float
        Equivalent dose in mg of the target steroid.
    

**Input Parameters**:
```json
{
  "properties": {
    "from_steroid": {
      "title": "From Steroid",
      "type": "string"
    },
    "from_dose_mg": {
      "title": "From Dose Mg",
      "type": "number"
    },
    "to_steroid": {
      "title": "To Steroid",
      "type": "string"
    }
  },
  "required": [
    "from_steroid",
    "from_dose_mg",
    "to_steroid"
  ],
  "title": "steroid_conversionArguments",
  "type": "object"
}
```

#### calculate_mme

**Description**: 
    Calculates total daily Morphine Milligram Equivalents (MME).

    Parameters:
    -----------
    opioid : str
        Name of the opioid (e.g., 'oxycodone', 'fentanyl_patch').
    dose_per_administration : float
        Amount of opioid per dose (mg for most, mcg/hr for fentanyl patch).
    doses_per_day : int
        Number of times the dose is taken per day.

    Returns:
    --------
    float
        Total MME/day.
    

**Input Parameters**:
```json
{
  "properties": {
    "opioid": {
      "title": "Opioid",
      "type": "string"
    },
    "dose_per_administration": {
      "title": "Dose Per Administration",
      "type": "number"
    },
    "doses_per_day": {
      "title": "Doses Per Day",
      "type": "integer"
    }
  },
  "required": [
    "opioid",
    "dose_per_administration",
    "doses_per_day"
  ],
  "title": "calculate_mmeArguments",
  "type": "object"
}
```

#### maintenance_fluids

**Description**: 
    Calculates maintenance IV fluid rate (mL/hr) using the 4-2-1 Rule.

    Parameters:
    -----------
    weight_kg : float
        Patient's weight in kilograms.

    Returns:
    --------
    float
        Maintenance fluid rate in mL/hr.
    

**Input Parameters**:
```json
{
  "properties": {
    "weight_kg": {
      "title": "Weight Kg",
      "type": "number"
    }
  },
  "required": [
    "weight_kg"
  ],
  "title": "maintenance_fluidsArguments",
  "type": "object"
}
```

#### corrected_sodium

**Description**: 
    Calculates corrected sodium level in the setting of hyperglycemia
    using Katz and Hillier correction formulas.

    Parameters:
    -----------
    measured_sodium : float
        Measured serum sodium in mEq/L.
    serum_glucose : float
        Serum glucose in mg/dL.

    Returns:
    --------
    dict
        Dictionary with corrected sodium values using Katz and Hillier formulas.
    

**Input Parameters**:
```json
{
  "properties": {
    "measured_sodium": {
      "title": "Measured Sodium",
      "type": "number"
    },
    "serum_glucose": {
      "title": "Serum Glucose",
      "type": "number"
    }
  },
  "required": [
    "measured_sodium",
    "serum_glucose"
  ],
  "title": "corrected_sodiumArguments",
  "type": "object"
}
```

#### meld_3

**Description**: 
    Calculates MELD 3.0 Score for liver disease transplant planning.

    Parameters:
    -----------
    age : int
        Patient age in years.
    female : bool
        True if patient is female.
    bilirubin : float
        Serum bilirubin in mg/dL.
    inr : float
        INR (International Normalized Ratio).
    creatinine : float
        Serum creatinine in mg/dL.
    albumin : float
        Serum albumin in g/dL.
    sodium : float
        Serum sodium in mEq/L.
    dialysis : bool
        True if patient had ≥2 dialysis sessions or 24h CVVHD in last 7 days.

    Returns:
    --------
    int
        MELD 3.0 score, rounded to the nearest whole number.
    

**Input Parameters**:
```json
{
  "properties": {
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "female": {
      "title": "Female",
      "type": "boolean"
    },
    "bilirubin": {
      "title": "Bilirubin",
      "type": "number"
    },
    "inr": {
      "title": "Inr",
      "type": "number"
    },
    "creatinine": {
      "title": "Creatinine",
      "type": "number"
    },
    "albumin": {
      "title": "Albumin",
      "type": "number"
    },
    "sodium": {
      "title": "Sodium",
      "type": "number"
    },
    "dialysis": {
      "title": "Dialysis",
      "type": "boolean"
    }
  },
  "required": [
    "age",
    "female",
    "bilirubin",
    "inr",
    "creatinine",
    "albumin",
    "sodium",
    "dialysis"
  ],
  "title": "meld_3Arguments",
  "type": "object"
}
```

#### framingham_risk_score

**Description**: 
    Calculates the Framingham Risk Score for 10-year risk of heart attack (CHD)
    based on the Framingham Heart Study equation (men and women).

    Parameters:
    -----------
    age : int
        Age of the patient (30-79 years).
    total_cholesterol : float
        Total cholesterol in mg/dL.
    hdl_cholesterol : float
        HDL cholesterol in mg/dL.
    systolic_bp : float
        Systolic blood pressure in mmHg.
    treated_for_bp : bool
        Whether the patient is treated for high blood pressure (1 if yes, 0 if no).
    smoker : bool
        Whether the patient is a smoker (1 if yes, 0 if no).
    gender : str
        Gender of the patient ("male" or "female").

    Returns:
    --------
    float
        10-year risk of heart attack as a percentage.
    

**Input Parameters**:
```json
{
  "properties": {
    "age": {
      "title": "Age",
      "type": "integer"
    },
    "total_cholesterol": {
      "title": "Total Cholesterol",
      "type": "number"
    },
    "hdl_cholesterol": {
      "title": "Hdl Cholesterol",
      "type": "number"
    },
    "systolic_bp": {
      "title": "Systolic Bp",
      "type": "number"
    },
    "treated_for_bp": {
      "title": "Treated For Bp",
      "type": "boolean"
    },
    "smoker": {
      "title": "Smoker",
      "type": "boolean"
    },
    "gender": {
      "title": "Gender",
      "type": "string"
    }
  },
  "required": [
    "age",
    "total_cholesterol",
    "hdl_cholesterol",
    "systolic_bp",
    "treated_for_bp",
    "smoker",
    "gender"
  ],
  "title": "framingham_risk_scoreArguments",
  "type": "object"
}
```

#### homa_ir

**Description**: 
    Calculates the HOMA-IR score for insulin resistance.

    Formula:
    Score = (Fasting insulin (uIU/mL) * Fasting glucose (mg/dL)) / 405

    Parameters:
    -----------
    fasting_insulin : float
        Fasting insulin level in micro-units per milliliter (uIU/mL).
    fasting_glucose : float
        Fasting glucose level in milligrams per deciliter (mg/dL).

    Returns:
    --------
    float
        HOMA-IR score.
    

**Input Parameters**:
```json
{
  "properties": {
    "fasting_insulin": {
      "title": "Fasting Insulin",
      "type": "number"
    },
    "fasting_glucose": {
      "title": "Fasting Glucose",
      "type": "number"
    }
  },
  "required": [
    "fasting_insulin",
    "fasting_glucose"
  ],
  "title": "homa_irArguments",
  "type": "object"
}
```

---

###  Metropolitan Museum

**Description**: 

**Connection Status**: success

**Available Tools** (3 ):

#### list-departments

**Description**: List all departments in the Metropolitan Museum of Art (Met Museum)

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "__intent": {
      "type": "string",
      "description": "In ≤ 30 words, describe why you are calling this tool and how its result advances your overall task. Don't use first-person pronouns like \"I\" or \"my\". Make sure to give a gist of the whole task and how this tool fits into it."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#",
  "required": [
    "__intent"
  ]
}
```

#### search-museum-objects

**Description**: Search for objects in the Metropolitan Museum of Art (Met Museum). Will return Total objects found, followed by a list of Object Ids.The parameter title should be set to true if you want to search for objects by title.The parameter hasImages is false by default, but can be set to true to return objects without images.If the parameter hasImages is true, the parameter title should be false.

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "The search query, Returns a listing of all Object IDs for objects that contain the search query within the object's data"
    },
    "hasImages": {
      "type": "boolean",
      "default": false,
      "description": "Only returns objects that have images"
    },
    "title": {
      "type": "boolean",
      "default": false,
      "description": "This should be set to true if you want to search for objects by title"
    },
    "departmentId": {
      "type": "number",
      "description": "Returns objects that are in the specified department. The departmentId should come from the 'list-departments' tool."
    },
    "__intent": {
      "type": "string",
      "description": "In ≤ 30 words, describe why you are calling this tool and how its result advances your overall task. Don't use first-person pronouns like \"I\" or \"my\". Make sure to give a gist of the whole task and how this tool fits into it."
    }
  },
  "required": [
    "q",
    "__intent"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

#### get-museum-object

**Description**: Get a museum object by its ID, from the Metropolitan Museum of Art Collection

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "objectId": {
      "type": "number",
      "description": "The ID of the museum object to retrieve"
    },
    "returnImage": {
      "type": "boolean",
      "default": true,
      "description": "Whether to return the image (if available) of the object and add it to the server resources"
    },
    "__intent": {
      "type": "string",
      "description": "In ≤ 30 words, describe why you are calling this tool and how its result advances your overall task. Don't use first-person pronouns like \"I\" or \"my\". Make sure to give a gist of the whole task and how this tool fits into it."
    }
  },
  "required": [
    "objectId",
    "__intent"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

---

###  Movie Recommender

**Description**: 

**Connection Status**: success

**Available Tools** (1 ):

#### get_movies

**Description**: 
    Get movie suggestions based on keyword.
    

**Input Parameters**:
```json
{
  "properties": {
    "keyword": {
      "title": "Keyword",
      "type": "string"
    }
  },
  "required": [
    "keyword"
  ],
  "title": "get_moviesArguments",
  "type": "object"
}
```

---

###  NASA Data

**Description**: 

**Connection Status**: success

**Available Tools** (21 ):

#### get_astronomy_picture_of_day

**Description**: Get NASA's astronomy picture of the day.

Args:
    date: Date of the image in YYYY-MM-DD format. If not specified, the current date is used.
    count: If specified, returns 'count' random images. Cannot be used with 'date'.
    thumbs: If True, returns the thumbnail URL for videos. If APOD is not a video, this parameter is ignored.


**Input Parameters**:
```json
{
  "properties": {
    "date": {
      "default": null,
      "title": "Date",
      "type": "string"
    },
    "count": {
      "default": null,
      "title": "Count",
      "type": "integer"
    },
    "thumbs": {
      "default": false,
      "title": "Thumbs",
      "type": "boolean"
    }
  },
  "title": "get_astronomy_picture_of_dayArguments",
  "type": "object"
}
```

#### get_asteroids_feed

**Description**: Get a list of asteroids based on their closest approach date to Earth.

Args:
    start_date: Start date for asteroid search in YYYY-MM-DD format.
    end_date: End date for asteroid search in YYYY-MM-DD format. 
    The Feed date limit is only 7 Days. If not specified, 7 days after start_date is used.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "required": [
    "start_date"
  ],
  "title": "get_asteroids_feedArguments",
  "type": "object"
}
```

#### get_asteroid_lookup

**Description**: Look up a specific asteroid based on its NASA JPL ID.

Args:
    asteroid_id: Asteroid ID in the NASA JPL small body (SPK-ID) system.


**Input Parameters**:
```json
{
  "properties": {
    "asteroid_id": {
      "title": "Asteroid Id",
      "type": "string"
    }
  },
  "required": [
    "asteroid_id"
  ],
  "title": "get_asteroid_lookupArguments",
  "type": "object"
}
```

#### browse_asteroids

**Description**: Browse the asteroid dataset.

**Input Parameters**:
```json
{
  "properties": {},
  "title": "browse_asteroidsArguments",
  "type": "object"
}
```

#### get_coronal_mass_ejection

**Description**: Get coronal mass ejection (CME) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_coronal_mass_ejectionArguments",
  "type": "object"
}
```

#### get_geomagnetic_storm

**Description**: Get geomagnetic storm (GST) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_geomagnetic_stormArguments",
  "type": "object"
}
```

#### get_solar_flare

**Description**: Get solar flare (FLR) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_solar_flareArguments",
  "type": "object"
}
```

#### get_solar_energetic_particle

**Description**: Get solar energetic particle (SEP) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_solar_energetic_particleArguments",
  "type": "object"
}
```

#### get_magnetopause_crossing

**Description**: Get magnetopause crossing (MPC) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_magnetopause_crossingArguments",
  "type": "object"
}
```

#### get_radiation_belt_enhancement

**Description**: Get radiation belt enhancement (RBE) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_radiation_belt_enhancementArguments",
  "type": "object"
}
```

#### get_hight_speed_stream

**Description**: Get high speed stream (HSS) data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 30 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_hight_speed_streamArguments",
  "type": "object"
}
```

#### get_wsa_enlil_simulation

**Description**: Get WSA+Enlil simulation data.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 7 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    }
  },
  "title": "get_wsa_enlil_simulationArguments",
  "type": "object"
}
```

#### get_notifications

**Description**: Get DONKI notifications.

Args:
    start_date: Start date in YYYY-MM-DD format. Defaults to 7 days before current date.
    end_date: End date in YYYY-MM-DD format. Defaults to current date.
    notification_type: Notification type. Options: all, FLR, SEP, CME, IPS, MPC, GST, RBE, report.


**Input Parameters**:
```json
{
  "properties": {
    "start_date": {
      "default": null,
      "title": "Start Date",
      "type": "string"
    },
    "end_date": {
      "default": null,
      "title": "End Date",
      "type": "string"
    },
    "notification_type": {
      "default": "all",
      "title": "Notification Type",
      "type": "string"
    }
  },
  "title": "get_notificationsArguments",
  "type": "object"
}
```

#### get_earth_imagery

**Description**: Get Earth imagery from Landsat 8 satellite.

Args:
    lat: Latitude.
    lon: Longitude.
    date: Image date in YYYY-MM-DD format. If not specified, the most recent image is used.
    dim: Width and height of the image in degrees (0.025 degrees is approximately 2.7 km).
    cloud_score: Calculate the percentage of the image covered by clouds (currently not available).


**Input Parameters**:
```json
{
  "properties": {
    "lat": {
      "title": "Lat",
      "type": "number"
    },
    "lon": {
      "title": "Lon",
      "type": "number"
    },
    "date": {
      "default": null,
      "title": "Date",
      "type": "string"
    },
    "dim": {
      "default": 0.025,
      "title": "Dim",
      "type": "number"
    },
    "cloud_score": {
      "default": false,
      "title": "Cloud Score",
      "type": "boolean"
    }
  },
  "required": [
    "lat",
    "lon"
  ],
  "title": "get_earth_imageryArguments",
  "type": "object"
}
```

#### get_earth_assets

**Description**: Get information about available imagery assets for a specific location and date.

Args:
    lat: Latitude.
    lon: Longitude.
    date: Date in YYYY-MM-DD format.
    dim: Width and height of the image in degrees (0.025 degrees is approximately 2.7 km).


**Input Parameters**:
```json
{
  "properties": {
    "lat": {
      "title": "Lat",
      "type": "number"
    },
    "lon": {
      "title": "Lon",
      "type": "number"
    },
    "date": {
      "title": "Date",
      "type": "string"
    },
    "dim": {
      "default": 0.025,
      "title": "Dim",
      "type": "number"
    }
  },
  "required": [
    "lat",
    "lon",
    "date"
  ],
  "title": "get_earth_assetsArguments",
  "type": "object"
}
```

#### get_epic_imagery

**Description**: Get images from the EPIC (Earth Polychromatic Imaging Camera).

Args:
    collection: Collection type. Options: natural, enhanced.


**Input Parameters**:
```json
{
  "properties": {
    "collection": {
      "default": "natural",
      "title": "Collection",
      "type": "string"
    }
  },
  "title": "get_epic_imageryArguments",
  "type": "object"
}
```

#### get_epic_imagery_by_date

**Description**: Get images from the EPIC (Earth Polychromatic Imaging Camera) for a specific date.

Args:
    date: Date in YYYY-MM-DD format.
    collection: Collection type. Options: natural, enhanced.


**Input Parameters**:
```json
{
  "properties": {
    "date": {
      "title": "Date",
      "type": "string"
    },
    "collection": {
      "default": "natural",
      "title": "Collection",
      "type": "string"
    }
  },
  "required": [
    "date"
  ],
  "title": "get_epic_imagery_by_dateArguments",
  "type": "object"
}
```

#### get_epic_dates

**Description**: Get available dates for EPIC images.

Args:
    collection: Collection type. Options: natural, enhanced.


**Input Parameters**:
```json
{
  "properties": {
    "collection": {
      "default": "natural",
      "title": "Collection",
      "type": "string"
    }
  },
  "title": "get_epic_datesArguments",
  "type": "object"
}
```

#### get_exoplanet_data

**Description**: Get data from NASA's Exoplanet Archive.

Args:
    query: Specific query to filter results using Exoplanet Archive syntax. Example: "pl_orbper > 300 and pl_rade < 2"
    table: Table to query. Common options: exoplanets (confirmed planets), cumulative (Kepler Objects of Interest), koi (subset of cumulative), tce (Threshold Crossing Events).
    format: Output format. Options: json, csv, xml, ipac. Default: json.


**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "default": null,
      "title": "Query",
      "type": "string"
    },
    "table": {
      "default": "exoplanets",
      "title": "Table",
      "type": "string"
    },
    "format": {
      "default": "json",
      "title": "Format",
      "type": "string"
    }
  },
  "title": "get_exoplanet_dataArguments",
  "type": "object"
}
```

#### get_mars_rover_photos

**Description**: Get photos from a Mars rover (Curiosity, Opportunity, Spirit).
Specify either sol (Martian day) or earth_date (YYYY-MM-DD), but not both.

Args:
    rover_name: Name of the rover (curiosity, opportunity, spirit).
    sol: Martian sol (day number, starting from landing). Use if not using earth_date.
    earth_date: Earth date in YYYY-MM-DD format. Use if not using sol.
    camera: Filter by camera abbreviation (e.g., FHAZ, RHAZ, MAST, NAVCAM, PANCAM). See documentation for full list per rover.
    page: Page number for results (25 photos per page).


**Input Parameters**:
```json
{
  "properties": {
    "rover_name": {
      "title": "Rover Name",
      "type": "string"
    },
    "sol": {
      "default": null,
      "title": "Sol",
      "type": "integer"
    },
    "earth_date": {
      "default": null,
      "title": "Earth Date",
      "type": "string"
    },
    "camera": {
      "default": null,
      "title": "Camera",
      "type": "string"
    },
    "page": {
      "default": 1,
      "title": "Page",
      "type": "integer"
    }
  },
  "required": [
    "rover_name"
  ],
  "title": "get_mars_rover_photosArguments",
  "type": "object"
}
```

#### get_mars_rover_manifest

**Description**: Get the mission manifest for a Mars rover (Curiosity, Opportunity, Spirit).
Provides mission details like landing/launch dates, status, max sol/date, total photos, and photo counts per sol.

Args:
    rover_name: Name of the rover (curiosity, opportunity, spirit).


**Input Parameters**:
```json
{
  "properties": {
    "rover_name": {
      "title": "Rover Name",
      "type": "string"
    }
  },
  "required": [
    "rover_name"
  ],
  "title": "get_mars_rover_manifestArguments",
  "type": "object"
}
```

---

###  OKX Exchange

**Description**: 

**Connection Status**: success

**Available Tools** (2 ):

#### get_price

**Description**: Get latest price for an OKX instrument

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "instrument": {
      "type": "string",
      "description": "Instrument ID (e.g. BTC-USDT)"
    }
  },
  "required": [
    "instrument"
  ]
}
```

#### get_candlesticks

**Description**: Get candlestick data for an OKX instrument

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "instrument": {
      "type": "string",
      "description": "Instrument ID (e.g. BTC-USDT)"
    },
    "bar": {
      "type": "string",
      "description": "Time interval (e.g. 1m, 5m, 1H, 1D)",
      "default": "1m"
    },
    "limit": {
      "type": "number",
      "description": "Number of candlesticks (max 100)",
      "default": 100
    }
  },
  "required": [
    "instrument"
  ]
}
```

---

###  Paper Search

**Description**: 

**Connection Status**: success

**Available Tools** (19 ):

#### search_arxiv

**Description**: Search academic papers from arXiv.

Args:
    query: Search query string (e.g., 'machine learning').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### search_pubmed

**Description**: Search academic papers from PubMed.

Args:
    query: Search query string (e.g., 'machine learning').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### search_biorxiv

**Description**: Search academic papers from bioRxiv.

Args:
    query: Search query string (e.g., 'machine learning').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### search_medrxiv

**Description**: Search academic papers from medRxiv.

Args:
    query: Search query string (e.g., 'machine learning').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### search_google_scholar

**Description**: Search academic papers from Google Scholar.

Args:
    query: Search query string (e.g., 'machine learning').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### search_iacr

**Description**: Search academic papers from IACR ePrint Archive.

Args:
    query: Search query string (e.g., 'cryptography', 'secret sharing').
    max_results: Maximum number of papers to return (default: 10).
    fetch_details: Whether to fetch detailed information for each paper (default: True).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    },
    "fetch_details": {
      "default": true,
      "type": "boolean"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### download_arxiv

**Description**: Download PDF of an arXiv paper.

Args:
    paper_id: arXiv paper ID (e.g., '2106.12345').
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    Path to the downloaded PDF file.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### download_pubmed

**Description**: Attempt to download PDF of a PubMed paper.

Args:
    paper_id: PubMed ID (PMID).
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    str: Message indicating that direct PDF download is not supported.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### download_biorxiv

**Description**: Download PDF of a bioRxiv paper.

Args:
    paper_id: bioRxiv DOI.
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    Path to the downloaded PDF file.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### download_medrxiv

**Description**: Download PDF of a medRxiv paper.

Args:
    paper_id: medRxiv DOI.
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    Path to the downloaded PDF file.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### download_iacr

**Description**: Download PDF of an IACR ePrint paper.

Args:
    paper_id: IACR paper ID (e.g., '2009/101').
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    Path to the downloaded PDF file.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_arxiv_paper

**Description**: Read and extract text content from an arXiv paper PDF.

Args:
    paper_id: arXiv paper ID (e.g., '2106.12345').
    save_path: Directory where the PDF is/will be saved (default: './downloads').
Returns:
    str: The extracted text content of the paper.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_pubmed_paper

**Description**: Read and extract text content from a PubMed paper.

Args:
    paper_id: PubMed ID (PMID).
    save_path: Directory where the PDF would be saved (unused).
Returns:
    str: Message indicating that direct paper reading is not supported.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_biorxiv_paper

**Description**: Read and extract text content from a bioRxiv paper PDF.

Args:
    paper_id: bioRxiv DOI.
    save_path: Directory where the PDF is/will be saved (default: './downloads').
Returns:
    str: The extracted text content of the paper.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_medrxiv_paper

**Description**: Read and extract text content from a medRxiv paper PDF.

Args:
    paper_id: medRxiv DOI.
    save_path: Directory where the PDF is/will be saved (default: './downloads').
Returns:
    str: The extracted text content of the paper.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_iacr_paper

**Description**: Read and extract text content from an IACR ePrint paper PDF.

Args:
    paper_id: IACR paper ID (e.g., '2009/101').
    save_path: Directory where the PDF is/will be saved (default: './downloads').
Returns:
    str: The extracted text content of the paper.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### search_semantic

**Description**: Search academic papers from Semantic Scholar.

Args:
    query: Search query string (e.g., 'machine learning').
    year: Optional year filter (e.g., '2019', '2016-2020', '2010-', '-2015').
    max_results: Maximum number of papers to return (default: 10).
Returns:
    List of paper metadata in dictionary format.

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "type": "string"
    },
    "year": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null
    },
    "max_results": {
      "default": 10,
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "type": "object"
}
```

#### download_semantic

**Description**: Download PDF of a Semantic Scholar paper.    

Args:
    paper_id: Semantic Scholar paper ID, Paper identifier in one of the following formats:
        - Semantic Scholar ID (e.g., "649def34f8be52c8b66281af98ae884c09aef38b")
        - DOI:<doi> (e.g., "DOI:10.18653/v1/N18-3011")
        - ARXIV:<id> (e.g., "ARXIV:2106.15928")
        - MAG:<id> (e.g., "MAG:112218234")
        - ACL:<id> (e.g., "ACL:W12-3903")
        - PMID:<id> (e.g., "PMID:19872477")
        - PMCID:<id> (e.g., "PMCID:2323736")
        - URL:<url> (e.g., "URL:https://arxiv.org/abs/2106.15928v1")
    save_path: Directory to save the PDF (default: './downloads').
Returns:
    Path to the downloaded PDF file.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

#### read_semantic_paper

**Description**: Read and extract text content from a Semantic Scholar paper. 

Args:
    paper_id: Semantic Scholar paper ID, Paper identifier in one of the following formats:
        - Semantic Scholar ID (e.g., "649def34f8be52c8b66281af98ae884c09aef38b")
        - DOI:<doi> (e.g., "DOI:10.18653/v1/N18-3011")
        - ARXIV:<id> (e.g., "ARXIV:2106.15928")
        - MAG:<id> (e.g., "MAG:112218234")
        - ACL:<id> (e.g., "ACL:W12-3903")
        - PMID:<id> (e.g., "PMID:19872477")
        - PMCID:<id> (e.g., "PMCID:2323736")
        - URL:<url> (e.g., "URL:https://arxiv.org/abs/2106.15928v1")
    save_path: Directory where the PDF is/will be saved (default: './downloads').
Returns:
    str: The extracted text content of the paper.

**Input Parameters**:
```json
{
  "properties": {
    "paper_id": {
      "type": "string"
    },
    "save_path": {
      "default": "./downloads",
      "type": "string"
    }
  },
  "required": [
    "paper_id"
  ],
  "type": "object"
}
```

---

###  Scientific Computing

**Description**: 

**Connection Status**: success

**Available Tools** (26 ):

#### create_tensor

**Description**: 
    Creates a NumPy array (matrix) with a specified shape and values.

    Args:
        shape (list[int]): The shape of the resulting array as a tuple(e.g., (2, 3)).
        values (list[float]): A flat list of values to populate the array.
        name (str): The name of the tensor to be stored.

    Returns:
        np.ndarray: A NumPy array with the specified shape.

    Raises:
        ValueError: If the number of values does not match the product of the shape.
    

**Input Parameters**:
```json
{
  "properties": {
    "shape": {
      "description": "Tensor shape as list of integers",
      "items": {
        "type": "integer"
      },
      "minItems": 1,
      "title": "Shape",
      "type": "array"
    },
    "values": {
      "description": "Flat list of floats to fill the tensor",
      "items": {
        "type": "number"
      },
      "minItems": 1,
      "title": "Values",
      "type": "array"
    },
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "shape",
    "values",
    "name"
  ],
  "title": "create_tensorArguments",
  "type": "object"
}
```

#### view_tensor

**Description**: 
    Returns an immutable view of a previously stored NumPy tensor from the in-memory tensor store.

    Args:
        name (str): The name of the tensor as stored in the in-store dictionary
    Returns:
        dict: The in-store dictionary for tensors

    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "view_tensorArguments",
  "type": "object"
}
```

#### delete_tensor

**Description**: 
    Deletes a tensor from the in-memory tensor store.

    Args:
        name (str): The name of the tensor to delete.

    Raises:
        ValueError: If the tensor name is not found in the store or if an error occurs during deletion.
    

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "delete_tensorArguments",
  "type": "object"
}
```

#### add_matrices

**Description**: 
        Adds two stored tensors element-wise.

        Args:
            name_a (str): The name of the first tensor.
            name_b (str): The name of the second tensor.

        Returns:
            np.ndarray: The result of element-wise addition.

        Raises:
            ValueError: If the tensor names are not found or shapes are incompatible.
        

**Input Parameters**:
```json
{
  "properties": {
    "name_a": {
      "title": "Name A",
      "type": "string"
    },
    "name_b": {
      "title": "Name B",
      "type": "string"
    }
  },
  "required": [
    "name_a",
    "name_b"
  ],
  "title": "add_matricesArguments",
  "type": "object"
}
```

#### subtract_matrices

**Description**: 
        Adds two stored tensors element-wise.

        Args:
            name_a (str): The name of the first tensor.
            name_b (str): The name of the second tensor.

        Returns:
            np.ndarray: The result of element-wise subtraction.

        Raises:
            ValueError: If the tensor names are not found or shapes are incompatible.
        

**Input Parameters**:
```json
{
  "properties": {
    "name_a": {
      "title": "Name A",
      "type": "string"
    },
    "name_b": {
      "title": "Name B",
      "type": "string"
    }
  },
  "required": [
    "name_a",
    "name_b"
  ],
  "title": "subtract_matricesArguments",
  "type": "object"
}
```

#### multiply_matrices

**Description**: 
        Performs matrix multiplication between two stored tensors.

        Args:
            name_a (str): The name of the first tensor.
            name_b (str): The name of the second tensor.

        Returns:
            np.ndarray: The result of matrix multiplication.

        Raises:
            ValueError: If either tensor is not found or their shapes are incompatible.
        

**Input Parameters**:
```json
{
  "properties": {
    "name_a": {
      "title": "Name A",
      "type": "string"
    },
    "name_b": {
      "title": "Name B",
      "type": "string"
    }
  },
  "required": [
    "name_a",
    "name_b"
  ],
  "title": "multiply_matricesArguments",
  "type": "object"
}
```

#### scale_matrix

**Description**: 
        Scales a stored tensor by a scalar factor.

        Args:
            name (str): The name of the tensor to scale.
            scale_factor (float): The scalar value to multiply the tensor by.
            in_place (bool): If True, updates the stored tensor; otherwise, returns a new scaled tensor.

        Returns:
            np.ndarray: The scaled tensor.

        Raises:
            ValueError: If the tensor name is not found in the store.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "scale_factor": {
      "title": "Scale Factor",
      "type": "number"
    },
    "in_place": {
      "default": true,
      "title": "In Place",
      "type": "boolean"
    }
  },
  "required": [
    "name",
    "scale_factor"
  ],
  "title": "scale_matrixArguments",
  "type": "object"
}
```

#### matrix_inverse

**Description**: 
        Computes the inverse of a stored square matrix.

        Args:
            name (str): The name of the tensor to invert.

        Returns:
            np.ndarray: The inverse of the matrix.

        Raises:
            ValueError: If the matrix is not found, is not square, or is singular (non-invertible).
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "matrix_inverseArguments",
  "type": "object"
}
```

#### transpose

**Description**: 
        Computes the transpose of a stored tensor.

        Args:
            name (str): The name of the tensor to transpose.

        Returns:
            np.ndarray: The transposed tensor.

        Raises:
            ValueError: If the tensor name is not found in the store.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "transposeArguments",
  "type": "object"
}
```

#### determinant

**Description**: 
        Computes the determinant of a stored square matrix.

        Args:
            name (str): The name of the matrix.

        Returns:
            float: The determinant of the matrix.

        Raises:
            ValueError: If the matrix is not found or is not square.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "determinantArguments",
  "type": "object"
}
```

#### rank

**Description**: 
        Computes the rank of a stored tensor.

        Args:
            name (str): The name of the tensor.

        Returns:
            int | list[int]: The rank of the matrix.

        Raises:
            ValueError: If the tensor name is not found in the store.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "rankArguments",
  "type": "object"
}
```

#### compute_eigen

**Description**: 
        Computes the eigenvalues and right eigenvectors of a stored square matrix.

        Args:
            name (str): The name of the tensor to analyze.

        Returns:
            dict: A dictionary with keys:
                - 'eigenvalues': np.ndarray
                - 'eigenvectors': np.ndarray

        Raises:
            ValueError: If the tensor is not found or is not a square matrix.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "compute_eigenArguments",
  "type": "object"
}
```

#### qr_decompose

**Description**: 
        Computes the QR decomposition of a stored matrix.

        Decomposes the matrix A into A = Q @ R, where Q is an orthogonal matrix
        and R is an upper triangular matrix.

        Args:
            name (str): The name of the matrix to decompose.

        Returns:
            dict: A dictionary with keys:
                - 'q': np.ndarray, the orthogonal matrix Q
                - 'r': np.ndarray, the upper triangular matrix R

        Raises:
            ValueError: If the matrix is not found or decomposition fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "qr_decomposeArguments",
  "type": "object"
}
```

#### svd_decompose

**Description**: 
        Computes the Singular Value Decomposition (SVD) of a stored matrix.

        Decomposes the matrix A into A = U @ S @ V^T, where U and V^T are orthogonal
        matrices, and S is a diagonal matrix of singular values.

        Args:
            name (str): The name of the matrix to decompose.

        Returns:
            dict: A dictionary with keys:
                - 'u': np.ndarray, the left singular vectors
                - 's': np.ndarray, the singular values
                - 'v_t': np.ndarray, the right singular vectors transposed

        Raises:
            ValueError: If the matrix is not found or decomposition fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "svd_decomposeArguments",
  "type": "object"
}
```

#### find_orthonormal_basis

**Description**: 
        Finds an orthonormal basis for the column space of a stored matrix using QR decomposition.

        Args:
            name (str): The name of the matrix.

        Returns:
            list[list[float]]: A list of orthonormal basis vectors.

        Raises:
            ValueError: If the matrix is not found or decomposition fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "find_orthonormal_basisArguments",
  "type": "object"
}
```

#### change_basis

**Description**: 
        Changes the basis of a stored square matrix.

        Args:
            name (str): Name of the matrix in the tensor store.
            new_basis (list[list[float]]): Columns are new basis vectors.

        Returns:
            np.ndarray: Representation of the matrix in the new basis.

        Raises:
            ValueError: If the matrix name is not found or non-invertible.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "new_basis": {
      "items": {
        "items": {
          "type": "number"
        },
        "type": "array"
      },
      "title": "New Basis",
      "type": "array"
    }
  },
  "required": [
    "name",
    "new_basis"
  ],
  "title": "change_basisArguments",
  "type": "object"
}
```

#### vector_project

**Description**: 
        Projects a stored vector onto another vector.

        Args:
            name (str): Name of the stored vector to project.
            new_vector (list[float]): The vector to project onto.

        Returns:
            np.ndarray: The projection result vector.

        Raises:
            ValueError: If the vector name is not found or projection fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "new_vector": {
      "items": {
        "type": "number"
      },
      "title": "New Vector",
      "type": "array"
    }
  },
  "required": [
    "name",
    "new_vector"
  ],
  "title": "vector_projectArguments",
  "type": "object"
}
```

#### vector_dot_product

**Description**: 
        Computes the dot product between two stored vectors.

        Args:
            name_a (str): Name of the first vector in the tensor store.
            name_b (str): Name of the second vector in the tensor store.

        Returns:
            np.ndarray: Scalar result of the dot product.

        Raises:
            ValueError: If either vector is not found or if the dot product computation fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name_a": {
      "title": "Name A",
      "type": "string"
    },
    "name_b": {
      "title": "Name B",
      "type": "string"
    }
  },
  "required": [
    "name_a",
    "name_b"
  ],
  "title": "vector_dot_productArguments",
  "type": "object"
}
```

#### vector_cross_product

**Description**: 
        Computes the cross product of two stored vectors.

        Args:
            name_a (str): Name of the first vector in the tensor store.
            name_b (str): Name of the second vector in the tensor store.

        Returns:
            np.ndarray: Vector result of the cross product.

        Raises:
            ValueError: If either vector is not found or if the cross product computation fails.
        

**Input Parameters**:
```json
{
  "properties": {
    "name_a": {
      "title": "Name A",
      "type": "string"
    },
    "name_b": {
      "title": "Name B",
      "type": "string"
    }
  },
  "required": [
    "name_a",
    "name_b"
  ],
  "title": "vector_cross_productArguments",
  "type": "object"
}
```

#### gradient

**Description**: 
        Computes the symbolic gradient of a scalar function.

        Args:
            f_str (str): A string representing a scalar function (e.g., "x**2 + y*z").

        Returns:
            str: A string representation of the symbolic gradient as a vector.
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    }
  },
  "required": [
    "f_str"
  ],
  "title": "gradientArguments",
  "type": "object"
}
```

#### curl

**Description**: 
        Computes the symbolic curl of a vector field, optionally evaluated at a point.

        Args:
            f_str (str): A string representing the vector field in list format (e.g., "[x+y, x, 2*z]").
            point (list[float], optional): A list of coordinates [x, y, z] to evaluate the curl numerically.

        Returns:
            dict: A dictionary with the symbolic curl as a string, and optionally the evaluated vector.
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    },
    "point": {
      "default": null,
      "items": {
        "type": "number"
      },
      "title": "Point",
      "type": "array"
    }
  },
  "required": [
    "f_str"
  ],
  "title": "curlArguments",
  "type": "object"
}
```

#### divergence

**Description**: 
        Computes the symbolic divergence of a vector field, optionally evaluated at a point.

        Args:
            f_str (str): A string representing the vector field in list format (e.g., "[x+y, x, 2*z]").
            point (list[float], optional): A list of coordinates [x, y, z] to evaluate the divergence numerically.

        Returns:
            dict: A dictionary with the symbolic divergence as a string, and optionally the evaluated scalar.
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    },
    "point": {
      "default": null,
      "items": {
        "type": "number"
      },
      "title": "Point",
      "type": "array"
    }
  },
  "required": [
    "f_str"
  ],
  "title": "divergenceArguments",
  "type": "object"
}
```

#### laplacian

**Description**: 
        Computes the Laplacian of a scalar or vector field symbolically.

        Args:
            f_str (str): Scalar function as "x**2 + y*z" or vector "[Fx, Fy, Fz]".
            is_vector (bool): Set True to compute vector Laplacian.

        Returns:
            str: Symbolic result of the Laplacian—scalar or list of 3 components.
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    },
    "is_vector": {
      "default": false,
      "title": "Is Vector",
      "type": "boolean"
    }
  },
  "required": [
    "f_str"
  ],
  "title": "laplacianArguments",
  "type": "object"
}
```

#### directional_deriv

**Description**: 
        Computes symbolic directional derivative of scalar field along a vector direction.

        Args: f_str (str): Expression like "x*y*z". u (list[float]): Direction vector [vx, vy, vz]. unit (bool): True
        if u should be normalized before calculating directional derivative. Set to True by default.

        Returns:
            str: Symbolic result as string.
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    },
    "u": {
      "items": {
        "type": "number"
      },
      "title": "U",
      "type": "array"
    },
    "unit": {
      "default": true,
      "title": "Unit",
      "type": "boolean"
    }
  },
  "required": [
    "f_str",
    "u"
  ],
  "title": "directional_derivArguments",
  "type": "object"
}
```

#### plot_vector_field

**Description**: 
        Plots a 3D vector field from a string "[u(x,y,z), v(x,y,z), w(x,y,z)]"

        Args:
            f_str: string representation of 3D field, e.g. "[z, -y, x]".
            bounds: (xmin, xmax, ymin, ymax, zmin, zmax)
            n: grid resolution per axis

        Returns: Displayed Matplotlib 3D quiver plot (no image return needed)
        

**Input Parameters**:
```json
{
  "properties": {
    "f_str": {
      "title": "F Str",
      "type": "string"
    },
    "bounds": {
      "default": [
        -1,
        1,
        -1,
        1,
        -1,
        1
      ],
      "title": "bounds",
      "type": "string"
    },
    "n": {
      "default": 10,
      "title": "N",
      "type": "integer"
    }
  },
  "required": [
    "f_str"
  ],
  "title": "plot_vector_fieldArguments",
  "type": "object"
}
```

#### plot_function

**Description**: 
        Plots a 2D or 3D mathematical function from a symbolic expression string.

        Args:
            expr_str: string representation of a function in x or x and y,
                      e.g. "x**2" or "sin(sqrt(x**2 + y**2))"
            xlim: (xmin, xmax) range for x-axis
            ylim: (ymin, ymax) range for y-axis (used in 2D or 3D)
            grid: resolution of the plot grid

        Returns:
            A rendered Image of the function using Matplotlib.
            - 2D plot if the expression contains only x
            - 3D surface plot if the expression contains both x and y
        

**Input Parameters**:
```json
{
  "properties": {
    "expr_str": {
      "title": "Expr Str",
      "type": "string"
    },
    "xlim": {
      "default": [
        -5,
        5
      ],
      "maxItems": 2,
      "minItems": 2,
      "prefixItems": [
        {
          "type": "integer"
        },
        {
          "type": "integer"
        }
      ],
      "title": "Xlim",
      "type": "array"
    },
    "ylim": {
      "default": [
        -5,
        5
      ],
      "maxItems": 2,
      "minItems": 2,
      "prefixItems": [
        {
          "type": "integer"
        },
        {
          "type": "integer"
        }
      ],
      "title": "Ylim",
      "type": "array"
    },
    "grid": {
      "default": 200,
      "title": "grid",
      "type": "string"
    }
  },
  "required": [
    "expr_str"
  ],
  "title": "plot_functionArguments",
  "type": "object"
}
```

---

###  Weather Data

**Description**: 

**Connection Status**: success

**Available Tools** (4 ):

#### get_current_weather_tool

**Description**: 
    Get current weather information for a specific city.

    Args:
        city: Name of the city to get weather for

    Returns:
        Current weather data including temperature, conditions, humidity, wind, etc.
    

**Input Parameters**:
```json
{
  "properties": {
    "city": {
      "title": "City",
      "type": "string"
    }
  },
  "required": [
    "city"
  ],
  "title": "get_current_weather_toolArguments",
  "type": "object"
}
```

#### get_weather_forecast_tool

**Description**: 
    Get weather forecast for a specific city.

    Args:
        city: Name of the city to get forecast for
        days: Number of days to forecast (1-10, default: 3)

    Returns:
        Weather forecast data for the specified number of days
    

**Input Parameters**:
```json
{
  "properties": {
    "city": {
      "title": "City",
      "type": "string"
    },
    "days": {
      "default": 3,
      "title": "Days",
      "type": "integer"
    }
  },
  "required": [
    "city"
  ],
  "title": "get_weather_forecast_toolArguments",
  "type": "object"
}
```

#### search_locations_tool

**Description**: 
    Search for locations by name.

    Args:
        query: Location name or partial name to search for

    Returns:
        List of matching locations with their details
    

**Input Parameters**:
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_locations_toolArguments",
  "type": "object"
}
```

#### get_live_temp

**Description**: 
    Legacy tool: Get current temperature for a city (for backward compatibility).
    Use get_current_weather_tool for more detailed information.
    

**Input Parameters**:
```json
{
  "properties": {
    "city": {
      "title": "City",
      "type": "string"
    }
  },
  "required": [
    "city"
  ],
  "title": "get_live_tempArguments",
  "type": "object"
}
```

---

###  Time MCP

**Description**: 

**Connection Status**: success

**Available Tools** (2 ):

#### get_current_time

**Description**: Get current time in a specific timezones

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "timezone": {
      "type": "string",
      "description": "IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use 'America/New_York' as local timezone if no timezone provided by the user."
    }
  },
  "required": [
    "timezone"
  ]
}
```

#### convert_time

**Description**: Convert time between timezones

**Input Parameters**:
```json
{
  "type": "object",
  "properties": {
    "source_timezone": {
      "type": "string",
      "description": "Source IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use 'America/New_York' as local timezone if no source timezone provided by the user."
    },
    "time": {
      "type": "string",
      "description": "Time to convert in 24-hour format (HH:MM)"
    },
    "target_timezone": {
      "type": "string",
      "description": "Target IANA timezone name (e.g., 'Asia/Tokyo', 'America/San_Francisco'). Use 'America/New_York' as local timezone if no target timezone provided by the user."
    }
  },
  "required": [
    "source_timezone",
    "time",
    "target_timezone"
  ]
}
```

---

