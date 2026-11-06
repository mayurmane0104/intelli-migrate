# Streaming - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming)

---

# Streaming

The streaming utility handles datasets larger than the available memory as streaming data.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#key-features)

- Stream Amazon S3 objects with a file-like interface with minimal memory consumption
- Built-in popular data transformations to decompress and deserialize (gzip, CSV, and ZIP)
- Build your own data transformation and add it to the pipeline

## Background[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#background)

Within Lambda, processing S3 objects larger than the allocated amount of memory can lead to out of memory or timeout situations. For cost efficiency, your S3 objects may be encoded and compressed in various formats (*gzip, CSV, zip files, etc*), increasing the  amount of non-business logic and reliability risks.

Streaming utility makes this process easier by fetching parts of your data as you consume it, and transparently applying data transformations to the data stream. This allows you to process one, a few, or all rows of your large dataset while consuming a few MBs only.

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#getting-started)

### Streaming from a S3 object[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#streaming-from-a-s3-object)

With `S3Object`, you'll need the bucket, object key, and optionally a version ID to stream its content.

We will fetch parts of your data from S3 as you process each line, consuming only the absolute minimal amount of memory.

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

### Data transformations[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#data-transformations)

Think of data transformations like a data processing pipeline - apply one or more in order.

As data is streamed, you can apply transformations to your data like decompressing gzip content and deserializing a CSV into a dictionary.

For popular data transformations like CSV or Gzip, you can quickly enable it at the constructor level:

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

Alternatively, you can apply transformations later via the `transform` method. By default, it will return the transformed stream you can use to read its contents. If you prefer in-place modifications, use `in_place=True`.

## When is this useful?

In scenarios where you might have a reusable logic to apply common transformations. This might be a function or a class that receives an instance of `S3Object`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

Note that when using `in_place=True`, there is no return (`None`).

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

#### Handling ZIP files[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#handling-zip-files)

`ZipTransform` doesn't support combining other transformations.

This is because a Zip file contains multiple files while transformations apply to a single stream.

That said, you can still open a specific file as a stream, reading only the necessary bytes to extract it:

| Reading an individual file in the zip as a stream | |
|---|---|
| 1 2 3 4 5 6 7 8 | 
 | 

#### Built-in data transformations[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#built-in-data-transformations)

We provide popular built-in transformations that you can apply against your streaming data.

| Name | Description | Class name | 
|---|---|---|
| Gzip | Gunzips the stream of data using the [gzip library](https://docs.python.org/3/library/gzip.html) | GzipTransform | 
| Zip | Exposes the stream as a [ZipFile object](https://docs.python.org/3/library/zipfile.html) | ZipTransform | 
| CSV | Parses each CSV line as a CSV object, returning dictionary objects | CsvTransform | 

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#advanced)

### Skipping or reading backwards[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#skipping-or-reading-backwards)

`S3Object` implements [Python I/O interface](https://docs.python.org/3/tutorial/inputoutput.html). This means you can use `seek` to start reading contents of your file from any particular position, saving you processing time.

#### Reading backwards[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#reading-backwards)

For example, let's imagine you have a large CSV file, each row has a non-uniform size (bytes), and you want to read and process the last row only.

| non_uniform_sample.csv | |
|---|---|
| 1 2 3 4 | 
 | 

You found out the last row has exactly 30 bytes. We can use `seek()` to skip to the end of the file, read 30 bytes, then transform to CSV.

| Reading only the last CSV row | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 | 
 | 

#### Skipping[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#skipping)

What if we want to jump the first N rows?

You can also solve with `seek`, but let's take a large uniform CSV file to make this easier to grasp.

| uniform_sample.csv | |
|---|---|
| 1 2 3 4 | 
 | 

You found out that each row has 8 bytes, the header line has 21 bytes, and every new line has 1 byte. You want to skip the first 100 lines.

| Skipping the first 100 rows | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | 
 | 

### Custom options for data transformations[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#custom-options-for-data-transformations)

We will propagate additional options to the underlying implementation for each transform class.

| Name | Available options | 
|---|---|
| GzipTransform | [GzipFile constructor](https://docs.python.org/3/library/gzip.html#gzip.GzipFile) | 
| ZipTransform | [ZipFile constructor](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile) | 
| CsvTransform | [DictReader constructor](https://docs.python.org/3/library/csv.html#csv.DictReader) | 

For instance, take `ZipTransform`. You can use the `compression` parameter if you want to unzip an S3 object compressed with `LZMA`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

Or, if you want to load a tab-separated file (TSV), you can use the `delimiter` parameter in the `CsvTransform`:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

### Building your own data transformation[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#building-your-own-data-transformation)

You can build your own custom data transformation by extending the `BaseTransform` class. The `transform` method receives an `IO[bytes]` object, and you are responsible for returning an `IO[bytes]` object.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#testing-your-code)

### Asserting data transformations[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#asserting-data-transformations)

Create an input payload using `io.BytesIO` and assert the response of the transformation:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

## Known limitations[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#known-limitations)

### AWS X-Ray segment size limit[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/streaming/#aws-x-ray-segment-size-limit)

We make multiple API calls to S3 as you read chunks from your S3 object. If your function is decorated with [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/), you can easily hit [AWS X-Ray 64K segment size](https://docs.aws.amazon.com/general/latest/gr/xray.html#limits_xray) when processing large files.

Use tracer decorators in parts where you don't read your `S3Object` instead.