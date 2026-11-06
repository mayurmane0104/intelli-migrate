# Streaming - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/streaming](https://docs.aws.amazon.com/powertools/python/latest/api_doc/streaming)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

def__init__(self,bucket:str,key:str,version_id:str|None=None,boto3_client:S3Client|None=None,is_gzip:bool|None=False,is_csv:bool|None=False,**sdk_options,):self.bucket=bucketself.key=keyself.version_id=version_id# The underlying seekable IO, where all the magic happensself.raw_stream=_S3SeekableIO(bucket=bucket,key=key,version_id=version_id,boto3_client=boto3_client,**sdk_options,)# Stores the list of data transformationsself._data_transformations:list[BaseTransform]=[]ifis_gzip:self._data_transformations.append(GzipTransform())ifis_csv:self._data_transformations.append(CsvTransform())# Stores the cached transformed streamself._transformed_stream:IO[bytes]|None=None

deftransform(self,transformations:BaseTransform[T]|Sequence[BaseTransform[T]],in_place:bool|None=False,)->T|None:""" Applies one or more data transformations to the stream. Parameters ---------- transformations: BaseTransform[T] | Sequence[BaseTransform[T]] One or more transformations to apply. Transformations are applied in the same order as they are declared. in_place: bool, optional Transforms the stream in place, instead of returning a new stream object. Defaults to false. Returns ------- T[bound=IO[bytes]], optional If in_place is False, returns an IO[bytes] object representing the transformed stream """# Make transformations always be a sequence to make mypy happyifnotisinstance(transformations,Sequence):transformations=[transformations]# Scenario 1: user wants to transform the stream in place.# In this case, we store the transformations and invalidate any existing transformed stream.# This way, the transformed_stream is re-created on the next IO operation.# This can happen when the user calls .transform multiple times before they start reading data## >>> s3object.transform(GzipTransform(), in_place=True)# >>> s3object.seek(0, io.SEEK_SET) <- this creates a transformed stream# >>> s3object.transform(CsvTransform(), in_place=True) <- need to re-create transformed stream# >>> s3object.read...ifin_place:self._data_transformations.extend(transformations)# Invalidate any existing transformed stream.# It will be created again next time it's accessed.self._transformed_stream=NonereturnNoneelse:# Tell mypy that raw_stream actually implements T (bound to IO[bytes])stream=cast(T,self.raw_stream)fortransformationintransformations:stream=transformation.transform(stream)returnstream

Returns a csv.DictReader that reads data from the input stream:
https://docs.python.org/3/library/csv.html#csv.DictReader

Example

1234567

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import CsvTransform
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> csv_reader = s3object.transform(CsvTransform())
>>> for row in csv_reader:
>>> print(row)

Since the underlying stream of bytes needs to be converted into a stream of characters (Iterator[str]),
we wrap the input into an io.TextIOWrapper. This means you have control over the text encoding
and line termination options.

1234567

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import CsvTransform
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> csv_reader = s3object.transform(CsvTransform(encoding="utf-8", newline="\r\n"))
>>> for row in csv_reader:
>>> print(row)

Additional options passed on the constructor, will be pased to the csv.DictReader constructor.

1234567

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import CsvTransform
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> csv_reader = s3object.transform(CsvTransform(dialect="excel"))
>>> for row in csv_reader:
>>> print(row)

Source code in aws_lambda_powertools/utilities/streaming/transformations/base.py

Returns a zip.ZipFile that reads data from the input stream:
https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile

Example

12345678

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import ZipTransform
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> zip_reader = s3object.transform(ZipTransform())
>>> for file in zip_reader.namelist():
>>> print(file)
>>> zip_reader.extract(file)

Additional options passed on the constructor, will be pased to the is_csv.DictReader constructor.

123456789

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import ZipTransform
>>> import zipfile
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> zip_reader = s3object.transform(ZipTransform(compression=zipfile.ZIP_LZMA))
>>> for file in zip_reader.namelist():
>>> print(file)
>>> zip_reader.extract(file)

Currently, it's not possible to pipe the Zip file stream into another data transformation,
since a Zip file contains multiple files, and not a single stream. However, you can still
open a specific file as a stream, reading only the necessary bytes to extract it:

123456789

>>> from aws_lambda_powertools.utilities.streaming import S3Object
>>> from aws_lambda_powertools.utilities.streaming.transformations import ZipTransform
>>> import zipfile
>>>
>>> s3object = S3Object(bucket="bucket", key="key")
>>> zip_reader = s3object.transform(ZipTransform())
>>> with zip_reader.open("filename.txt") as f:
>>> for line in f:
>>> print(line)

Source code in aws_lambda_powertools/utilities/streaming/transformations/base.py