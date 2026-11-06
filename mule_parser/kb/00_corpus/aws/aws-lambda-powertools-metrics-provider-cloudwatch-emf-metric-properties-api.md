# aws_lambda_powertools.metrics.provider.cloudwatch_emf.metric_properties API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/metric_properties.html](https://docs.aws.amazon.com/powertools/python/latest/api/metrics/provider/cloudwatch_emf/metric_properties.html)

---

# Module `aws_lambda_powertools.metrics.provider.cloudwatch_emf.metric_properties`

## Classes

- `class MetricResolution (*args, **kwds)`
- 
## Expand source code`class MetricResolution(Enum): Standard = 60 High = 1`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var High`
- `var Standard`
 
- `class MetricUnit (*args, **kwds)`
- 
## Expand source code`class MetricUnit(Enum): Seconds = "Seconds" Microseconds = "Microseconds" Milliseconds = "Milliseconds" Bytes = "Bytes" Kilobytes = "Kilobytes" Megabytes = "Megabytes" Gigabytes = "Gigabytes" Terabytes = "Terabytes" Bits = "Bits" Kilobits = "Kilobits" Megabits = "Megabits" Gigabits = "Gigabits" Terabits = "Terabits" Percent = "Percent" Count = "Count" BytesPerSecond = "Bytes/Second" KilobytesPerSecond = "Kilobytes/Second" MegabytesPerSecond = "Megabytes/Second" GigabytesPerSecond = "Gigabytes/Second" TerabytesPerSecond = "Terabytes/Second" BitsPerSecond = "Bits/Second" KilobitsPerSecond = "Kilobits/Second" MegabitsPerSecond = "Megabits/Second" GigabitsPerSecond = "Gigabits/Second" TerabitsPerSecond = "Terabits/Second" CountPerSecond = "Count/Second" NoUnit = "None"`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var Bits`
- `var BitsPerSecond`
- `var Bytes`
- `var BytesPerSecond`
- `var Count`
- `var CountPerSecond`
- `var Gigabits`
- `var GigabitsPerSecond`
- `var Gigabytes`
- `var GigabytesPerSecond`
- `var Kilobits`
- `var KilobitsPerSecond`
- `var Kilobytes`
- `var KilobytesPerSecond`
- `var Megabits`
- `var MegabitsPerSecond`
- `var Megabytes`
- `var MegabytesPerSecond`
- `var Microseconds`
- `var Milliseconds`
- `var NoUnit`
- `var Percent`
- `var Seconds`
- `var Terabits`
- `var TerabitsPerSecond`
- `var Terabytes`
- `var TerabytesPerSecond`