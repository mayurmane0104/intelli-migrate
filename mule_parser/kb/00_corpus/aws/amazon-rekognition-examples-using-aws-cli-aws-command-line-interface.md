# Amazon Rekognition examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_rekognition_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_rekognition_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Rekognition.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `compare-faces`.

For more information, see [Comparing faces in images](https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html).

- **AWS CLI**
- 
            
                    **To compare faces in two images**The following `compare-faces`command compares faces in two images stored in an Amazon S3 bucket.`aws rekognition compare-faces \ --source-image '``{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"source.jpg"}}`' \ --target-image '`{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"target.jpg"}}`'Output: `{ "UnmatchedFaces": [], "FaceMatches": [ { "Face": { "BoundingBox": { "Width": 0.12368916720151901, "Top": 0.16007372736930847, "Left": 0.5901257991790771, "Height": 0.25140416622161865 }, "Confidence": 100.0, "Pose": { "Yaw": -3.7351467609405518, "Roll": -0.10309021919965744, "Pitch": 0.8637830018997192 }, "Quality": { "Sharpness": 95.51618957519531, "Brightness": 65.29893493652344 }, "Landmarks": [ { "Y": 0.26721030473709106, "X": 0.6204193830490112, "Type": "eyeLeft" }, { "Y": 0.26831310987472534, "X": 0.6776827573776245, "Type": "eyeRight" }, { "Y": 0.3514654338359833, "X": 0.6241428852081299, "Type": "mouthLeft" }, { "Y": 0.35258132219314575, "X": 0.6713621020317078, "Type": "mouthRight" }, { "Y": 0.3140771687030792, "X": 0.6428444981575012, "Type": "nose" } ] }, "Similarity": 100.0 } ], "SourceImageFace": { "BoundingBox": { "Width": 0.12368916720151901, "Top": 0.16007372736930847, "Left": 0.5901257991790771, "Height": 0.25140416622161865 }, "Confidence": 100.0 } }`For more information, see [Comparing Faces in Images](https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [CompareFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/compare-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-collection`.

For more information, see [Creating a collection](https://docs.aws.amazon.com/rekognition/latest/dg/create-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To create a collection**The following `create-collection`command creates a collection with the specified name.`aws rekognition create-collection \ --collection-id``"MyCollection"`Output: `{ "CollectionArn": "aws:rekognition:us-west-2:123456789012:collection/MyCollection", "FaceModelVersion": "4.0", "StatusCode": 200 }`For more information, see [Creating a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/create-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [CreateCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-collection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stream-processor`.

- **AWS CLI**
- 
            
                    **To create a new stream processor**The following `create-stream-processor`example creates a new stream processor with the specified configuration.`aws rekognition create-stream-processor --name``my-stream-processor`\ --input '`{"KinesisVideoStream":{"Arn":"arn:aws:kinesisvideo:us-west-2:123456789012:stream/macwebcam/1530559711205"}}`'\ --stream-processor-output '`{"KinesisDataStream":{"Arn":"arn:aws:kinesis:us-west-2:123456789012:stream/AmazonRekognitionRekStream"}}`'\ --role-arn`arn:aws:iam::123456789012:role/AmazonRekognitionDetect`\ --settings '`{"FaceSearch":{"CollectionId":"MyCollection","FaceMatchThreshold":85.5}}`'Output: `{ "StreamProcessorArn": "arn:aws:rekognition:us-west-2:123456789012:streamprocessor/my-stream-processor" }`For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [CreateStreamProcessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-stream-processor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-collection`.

For more information, see [Deleting a collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To delete a collection**The following `delete-collection`command deletes the specified collection.`aws rekognition delete-collection \ --collection-id``MyCollection`Output: `{ "StatusCode": 200 }`For more information, see [Deleting a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DeleteCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-collection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-faces`.

For more information, see [Deleting faces from a collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-faces-procedure.html).

- **AWS CLI**
- 
            
                    **To delete faces from a collection**The following `delete-faces`command deletes the specified face from a collection.`aws rekognition delete-faces \ --collection-id``MyCollection`--face-ids '`["0040279c-0178-436e-b70a-e61b074e96b0"]`'Output: `{ "DeletedFaces": [ "0040279c-0178-436e-b70a-e61b074e96b0" ] }`For more information, see [Deleting Faces from a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/delete-faces-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DeleteFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stream-processor`.

- **AWS CLI**
- 
            
                    **To delete a stream processor**The following `delete-stream-processor`command deletes the specified stream processor.`aws rekognition delete-stream-processor \ --name``my-stream-processor`This command produces no output. For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DeleteStreamProcessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-stream-processor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-collection`.

For more information, see [Describing a collection](https://docs.aws.amazon.com/rekognition/latest/dg/describe-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To describe a collection**The following `describe-collection`example displays the details about the specified collection.`aws rekognition describe-collection \ --collection-id``MyCollection`Output: `{ "FaceCount": 200, "CreationTimestamp": 1569444828.274, "CollectionARN": "arn:aws:rekognition:us-west-2:123456789012:collection/MyCollection", "FaceModelVersion": "4.0" }`For more information, see [Describing a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/describe-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DescribeCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-collection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stream-processor`.

- **AWS CLI**
- 
            
                    **To get information about a stream processor**The following `describe-stream-processor`command displays details about the specified stream processor.`aws rekognition describe-stream-processor \ --name``my-stream-processor`Output: `{ "Status": "STOPPED", "Name": "my-stream-processor", "LastUpdateTimestamp": 1532449292.712, "Settings": { "FaceSearch": { "FaceMatchThreshold": 80.0, "CollectionId": "my-collection" } }, "RoleArn": "arn:aws:iam::123456789012:role/AmazonRekognitionDetectStream", "StreamProcessorArn": "arn:aws:rekognition:us-west-2:123456789012:streamprocessor/my-stream-processpr", "Output": { "KinesisDataStream": { "Arn": "arn:aws:kinesis:us-west-2:123456789012:stream/AmazonRekognitionRekStream" } }, "Input": { "KinesisVideoStream": { "Arn": "arn:aws:kinesisvideo:us-west-2:123456789012:stream/macwebcam/123456789012" } }, "CreationTimestamp": 1532449292.712 }`For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DescribeStreamProcessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-stream-processor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-faces`.

For more information, see [Detecting faces in an image](https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html).

- **AWS CLI**
- 
            
                    **To detect faces in an image**The following `detect-faces`command detects faces in the specified image stored in an Amazon S3 bucket.`aws rekognition detect-faces \ --image '``{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"MyFriend.jpg"}}`' \ --attributes`"ALL"`Output: `{ "FaceDetails": [ { "Confidence": 100.0, "Eyeglasses": { "Confidence": 98.91107940673828, "Value": false }, "Sunglasses": { "Confidence": 99.7966537475586, "Value": false }, "Gender": { "Confidence": 99.56611633300781, "Value": "Male" }, "Landmarks": [ { "Y": 0.26721030473709106, "X": 0.6204193830490112, "Type": "eyeLeft" }, { "Y": 0.26831310987472534, "X": 0.6776827573776245, "Type": "eyeRight" }, { "Y": 0.3514654338359833, "X": 0.6241428852081299, "Type": "mouthLeft" }, { "Y": 0.35258132219314575, "X": 0.6713621020317078, "Type": "mouthRight" }, { "Y": 0.3140771687030792, "X": 0.6428444981575012, "Type": "nose" }, { "Y": 0.24662546813488007, "X": 0.6001564860343933, "Type": "leftEyeBrowLeft" }, { "Y": 0.24326619505882263, "X": 0.6303644776344299, "Type": "leftEyeBrowRight" }, { "Y": 0.23818562924861908, "X": 0.6146903038024902, "Type": "leftEyeBrowUp" }, { "Y": 0.24373626708984375, "X": 0.6640064716339111, "Type": "rightEyeBrowLeft" }, { "Y": 0.24877218902111053, "X": 0.7025929093360901, "Type": "rightEyeBrowRight" }, { "Y": 0.23938551545143127, "X": 0.6823262572288513, "Type": "rightEyeBrowUp" }, { "Y": 0.265746533870697, "X": 0.6112898588180542, "Type": "leftEyeLeft" }, { "Y": 0.2676128149032593, "X": 0.6317071914672852, "Type": "leftEyeRight" }, { "Y": 0.262735515832901, "X": 0.6201658248901367, "Type": "leftEyeUp" }, { "Y": 0.27025148272514343, "X": 0.6206279993057251, "Type": "leftEyeDown" }, { "Y": 0.268223375082016, "X": 0.6658390760421753, "Type": "rightEyeLeft" }, { "Y": 0.2672517001628876, "X": 0.687832236289978, "Type": "rightEyeRight" }, { "Y": 0.26383838057518005, "X": 0.6769183874130249, "Type": "rightEyeUp" }, { "Y": 0.27138751745224, "X": 0.676596462726593, "Type": "rightEyeDown" }, { "Y": 0.32283174991607666, "X": 0.6350004076957703, "Type": "noseLeft" }, { "Y": 0.3219289481639862, "X": 0.6567046642303467, "Type": "noseRight" }, { "Y": 0.3420318365097046, "X": 0.6450609564781189, "Type": "mouthUp" }, { "Y": 0.3664324879646301, "X": 0.6455618143081665, "Type": "mouthDown" }, { "Y": 0.26721030473709106, "X": 0.6204193830490112, "Type": "leftPupil" }, { "Y": 0.26831310987472534, "X": 0.6776827573776245, "Type": "rightPupil" }, { "Y": 0.26343393325805664, "X": 0.5946047306060791, "Type": "upperJawlineLeft" }, { "Y": 0.3543180525302887, "X": 0.6044883728027344, "Type": "midJawlineLeft" }, { "Y": 0.4084877669811249, "X": 0.6477024555206299, "Type": "chinBottom" }, { "Y": 0.3562754988670349, "X": 0.707981526851654, "Type": "midJawlineRight" }, { "Y": 0.26580461859703064, "X": 0.7234612107276917, "Type": "upperJawlineRight" } ], "Pose": { "Yaw": -3.7351467609405518, "Roll": -0.10309021919965744, "Pitch": 0.8637830018997192 }, "Emotions": [ { "Confidence": 8.74203109741211, "Type": "SURPRISED" }, { "Confidence": 2.501944065093994, "Type": "ANGRY" }, { "Confidence": 0.7378743290901184, "Type": "DISGUSTED" }, { "Confidence": 3.5296201705932617, "Type": "HAPPY" }, { "Confidence": 1.7162904739379883, "Type": "SAD" }, { "Confidence": 9.518536567687988, "Type": "CONFUSED" }, { "Confidence": 0.45474427938461304, "Type": "FEAR" }, { "Confidence": 72.79895782470703, "Type": "CALM" } ], "AgeRange": { "High": 48, "Low": 32 }, "EyesOpen": { "Confidence": 98.93987274169922, "Value": true }, "BoundingBox": { "Width": 0.12368916720151901, "Top": 0.16007372736930847, "Left": 0.5901257991790771, "Height": 0.25140416622161865 }, "Smile": { "Confidence": 93.4493179321289, "Value": false }, "MouthOpen": { "Confidence": 90.53053283691406, "Value": false }, "Quality": { "Sharpness": 95.51618957519531, "Brightness": 65.29893493652344 }, "Mustache": { "Confidence": 89.85221099853516, "Value": false }, "Beard": { "Confidence": 86.1991195678711, "Value": true } } ] }`For more information, see [Detecting Faces in an Image](https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DetectFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-labels`.

For more information, see [Detecting labels in an image](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html).

- **AWS CLI**
- 
            
                    **To detect a label in an image**The following `detect-labels`example detects scenes and objects in an image stored in an Amazon S3 bucket.`aws rekognition detect-labels \ --image '``{"S3Object":{"Bucket":"bucket","Name":"image"}}`'Output: `{ "Labels": [ { "Instances": [], "Confidence": 99.15271759033203, "Parents": [ { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Automobile" }, { "Instances": [], "Confidence": 99.15271759033203, "Parents": [ { "Name": "Transportation" } ], "Name": "Vehicle" }, { "Instances": [], "Confidence": 99.15271759033203, "Parents": [], "Name": "Transportation" }, { "Instances": [ { "BoundingBox": { "Width": 0.10616336017847061, "Top": 0.5039216876029968, "Left": 0.0037978808395564556, "Height": 0.18528179824352264 }, "Confidence": 99.15271759033203 }, { "BoundingBox": { "Width": 0.2429988533258438, "Top": 0.5251884460449219, "Left": 0.7309805154800415, "Height": 0.21577216684818268 }, "Confidence": 99.1286392211914 }, { "BoundingBox": { "Width": 0.14233611524105072, "Top": 0.5333095788955688, "Left": 0.6494812965393066, "Height": 0.15528248250484467 }, "Confidence": 98.48368072509766 }, { "BoundingBox": { "Width": 0.11086395382881165, "Top": 0.5354844927787781, "Left": 0.10355594009160995, "Height": 0.10271988064050674 }, "Confidence": 96.45606231689453 }, { "BoundingBox": { "Width": 0.06254628300666809, "Top": 0.5573825240135193, "Left": 0.46083059906959534, "Height": 0.053911514580249786 }, "Confidence": 93.65448760986328 }, { "BoundingBox": { "Width": 0.10105438530445099, "Top": 0.534368634223938, "Left": 0.5743985772132874, "Height": 0.12226245552301407 }, "Confidence": 93.06217193603516 }, { "BoundingBox": { "Width": 0.056389667093753815, "Top": 0.5235804319381714, "Left": 0.9427769780158997, "Height": 0.17163699865341187 }, "Confidence": 92.6864013671875 }, { "BoundingBox": { "Width": 0.06003860384225845, "Top": 0.5441341400146484, "Left": 0.22409997880458832, "Height": 0.06737709045410156 }, "Confidence": 90.4227066040039 }, { "BoundingBox": { "Width": 0.02848697081208229, "Top": 0.5107086896896362, "Left": 0, "Height": 0.19150497019290924 }, "Confidence": 86.65286254882812 }, { "BoundingBox": { "Width": 0.04067881405353546, "Top": 0.5566273927688599, "Left": 0.316415935754776, "Height": 0.03428703173995018 }, "Confidence": 85.36471557617188 }, { "BoundingBox": { "Width": 0.043411049991846085, "Top": 0.5394920110702515, "Left": 0.18293385207653046, "Height": 0.0893595889210701 }, "Confidence": 82.21705627441406 }, { "BoundingBox": { "Width": 0.031183116137981415, "Top": 0.5579366683959961, "Left": 0.2853088080883026, "Height": 0.03989990055561066 }, "Confidence": 81.0157470703125 }, { "BoundingBox": { "Width": 0.031113790348172188, "Top": 0.5504819750785828, "Left": 0.2580395042896271, "Height": 0.056484755128622055 }, "Confidence": 56.13441467285156 }, { "BoundingBox": { "Width": 0.08586374670267105, "Top": 0.5438792705535889, "Left": 0.5128012895584106, "Height": 0.08550430089235306 }, "Confidence": 52.37760925292969 } ], "Confidence": 99.15271759033203, "Parents": [ { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Car" }, { "Instances": [], "Confidence": 98.9914321899414, "Parents": [], "Name": "Human" }, { "Instances": [ { "BoundingBox": { "Width": 0.19360728561878204, "Top": 0.35072067379951477, "Left": 0.43734854459762573, "Height": 0.2742200493812561 }, "Confidence": 98.9914321899414 }, { "BoundingBox": { "Width": 0.03801717236638069, "Top": 0.5010883808135986, "Left": 0.9155802130699158, "Height": 0.06597328186035156 }, "Confidence": 85.02790832519531 } ], "Confidence": 98.9914321899414, "Parents": [], "Name": "Person" }, { "Instances": [], "Confidence": 93.24951934814453, "Parents": [], "Name": "Machine" }, { "Instances": [ { "BoundingBox": { "Width": 0.03561960905790329, "Top": 0.6468243598937988, "Left": 0.7850857377052307, "Height": 0.08878646790981293 }, "Confidence": 93.24951934814453 }, { "BoundingBox": { "Width": 0.02217046171426773, "Top": 0.6149078607559204, "Left": 0.04757237061858177, "Height": 0.07136218994855881 }, "Confidence": 91.5025863647461 }, { "BoundingBox": { "Width": 0.016197510063648224, "Top": 0.6274210214614868, "Left": 0.6472989320755005, "Height": 0.04955997318029404 }, "Confidence": 85.14686584472656 }, { "BoundingBox": { "Width": 0.020207518711686134, "Top": 0.6348286867141724, "Left": 0.7295016646385193, "Height": 0.07059963047504425 }, "Confidence": 83.34547424316406 }, { "BoundingBox": { "Width": 0.020280985161662102, "Top": 0.6171894669532776, "Left": 0.08744934946298599, "Height": 0.05297485366463661 }, "Confidence": 79.9981460571289 }, { "BoundingBox": { "Width": 0.018318990245461464, "Top": 0.623889148235321, "Left": 0.6836880445480347, "Height": 0.06730121374130249 }, "Confidence": 78.87144470214844 }, { "BoundingBox": { "Width": 0.021310249343514442, "Top": 0.6167286038398743, "Left": 0.004064912907779217, "Height": 0.08317798376083374 }, "Confidence": 75.89361572265625 }, { "BoundingBox": { "Width": 0.03604431077837944, "Top": 0.7030032277107239, "Left": 0.9254803657531738, "Height": 0.04569442570209503 }, "Confidence": 64.402587890625 }, { "BoundingBox": { "Width": 0.009834849275648594, "Top": 0.5821820497512817, "Left": 0.28094568848609924, "Height": 0.01964157074689865 }, "Confidence": 62.79907989501953 }, { "BoundingBox": { "Width": 0.01475677452981472, "Top": 0.6137543320655823, "Left": 0.5950819253921509, "Height": 0.039063986390829086 }, "Confidence": 59.40483474731445 } ], "Confidence": 93.24951934814453, "Parents": [ { "Name": "Machine" } ], "Name": "Wheel" }, { "Instances": [], "Confidence": 92.61514282226562, "Parents": [], "Name": "Road" }, { "Instances": [], "Confidence": 92.37877655029297, "Parents": [ { "Name": "Person" } ], "Name": "Sport" }, { "Instances": [], "Confidence": 92.37877655029297, "Parents": [ { "Name": "Person" } ], "Name": "Sports" }, { "Instances": [ { "BoundingBox": { "Width": 0.12326609343290329, "Top": 0.6332163214683533, "Left": 0.44815489649772644, "Height": 0.058117982000112534 }, "Confidence": 92.37877655029297 } ], "Confidence": 92.37877655029297, "Parents": [ { "Name": "Person" }, { "Name": "Sport" } ], "Name": "Skateboard" }, { "Instances": [], "Confidence": 90.62931060791016, "Parents": [ { "Name": "Person" } ], "Name": "Pedestrian" }, { "Instances": [], "Confidence": 88.81334686279297, "Parents": [], "Name": "Asphalt" }, { "Instances": [], "Confidence": 88.81334686279297, "Parents": [], "Name": "Tarmac" }, { "Instances": [], "Confidence": 88.23201751708984, "Parents": [], "Name": "Path" }, { "Instances": [], "Confidence": 80.26520538330078, "Parents": [], "Name": "Urban" }, { "Instances": [], "Confidence": 80.26520538330078, "Parents": [ { "Name": "Building" }, { "Name": "Urban" } ], "Name": "Town" }, { "Instances": [], "Confidence": 80.26520538330078, "Parents": [], "Name": "Building" }, { "Instances": [], "Confidence": 80.26520538330078, "Parents": [ { "Name": "Building" }, { "Name": "Urban" } ], "Name": "City" }, { "Instances": [], "Confidence": 78.37934875488281, "Parents": [ { "Name": "Car" }, { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Parking Lot" }, { "Instances": [], "Confidence": 78.37934875488281, "Parents": [ { "Name": "Car" }, { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Parking" }, { "Instances": [], "Confidence": 74.37590026855469, "Parents": [ { "Name": "Building" }, { "Name": "Urban" }, { "Name": "City" } ], "Name": "Downtown" }, { "Instances": [], "Confidence": 69.84622955322266, "Parents": [ { "Name": "Road" } ], "Name": "Intersection" }, { "Instances": [], "Confidence": 57.68518829345703, "Parents": [ { "Name": "Sports Car" }, { "Name": "Car" }, { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Coupe" }, { "Instances": [], "Confidence": 57.68518829345703, "Parents": [ { "Name": "Car" }, { "Name": "Vehicle" }, { "Name": "Transportation" } ], "Name": "Sports Car" }, { "Instances": [], "Confidence": 56.59492111206055, "Parents": [ { "Name": "Path" } ], "Name": "Sidewalk" }, { "Instances": [], "Confidence": 56.59492111206055, "Parents": [ { "Name": "Path" } ], "Name": "Pavement" }, { "Instances": [], "Confidence": 55.58770751953125, "Parents": [ { "Name": "Building" }, { "Name": "Urban" } ], "Name": "Neighborhood" } ], "LabelModelVersion": "2.0" }`For more information, see [Detecting Labels in an Image](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DetectLabels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-labels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-moderation-labels`.

For more information, see [Detecting inappropriate images](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-images.html).

- **AWS CLI**
- 
            
                    **To detect unsafe content in an image**The following `detect-moderation-labels`command detects unsafe content in the specified image stored in an Amazon S3 bucket.`aws rekognition detect-moderation-labels \ --image``"S3Object={Bucket=MyImageS3Bucket,Name=gun.jpg}"`Output: `{ "ModerationModelVersion": "3.0", "ModerationLabels": [ { "Confidence": 97.29618072509766, "ParentName": "Violence", "Name": "Weapon Violence" }, { "Confidence": 97.29618072509766, "ParentName": "", "Name": "Violence" } ] }`For more information, see [Detecting Unsafe Images](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-images.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [DetectModerationLabels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-moderation-labels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-text`.

For more information, see [Detecting text in an image](https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html).

- **AWS CLI**
- 
            
                    **To detect text in an image**The following `detect-text`command detects text in the specified image.`aws rekognition detect-text \ --image '``{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"ExamplePicture.jpg"}}`'Output: `{ "TextDetections": [ { "Geometry": { "BoundingBox": { "Width": 0.24624845385551453, "Top": 0.28288066387176514, "Left": 0.391388863325119, "Height": 0.022687450051307678 }, "Polygon": [ { "Y": 0.28288066387176514, "X": 0.391388863325119 }, { "Y": 0.2826388478279114, "X": 0.6376373171806335 }, { "Y": 0.30532628297805786, "X": 0.637677013874054 }, { "Y": 0.305568128824234, "X": 0.39142853021621704 } ] }, "Confidence": 94.35709381103516, "DetectedText": "ESTD 1882", "Type": "LINE", "Id": 0 }, { "Geometry": { "BoundingBox": { "Width": 0.33933889865875244, "Top": 0.32603850960731506, "Left": 0.34534579515457153, "Height": 0.07126858830451965 }, "Polygon": [ { "Y": 0.32603850960731506, "X": 0.34534579515457153 }, { "Y": 0.32633158564567566, "X": 0.684684693813324 }, { "Y": 0.3976001739501953, "X": 0.684575080871582 }, { "Y": 0.3973070979118347, "X": 0.345236212015152 } ] }, "Confidence": 99.95779418945312, "DetectedText": "BRAINS", "Type": "LINE", "Id": 1 }, { "Confidence": 97.22098541259766, "Geometry": { "BoundingBox": { "Width": 0.061079490929841995, "Top": 0.2843210697174072, "Left": 0.391391396522522, "Height": 0.021029088646173477 }, "Polygon": [ { "Y": 0.2843210697174072, "X": 0.391391396522522 }, { "Y": 0.2828207015991211, "X": 0.4524524509906769 }, { "Y": 0.3038259446620941, "X": 0.4534534513950348 }, { "Y": 0.30532634258270264, "X": 0.3923923969268799 } ] }, "DetectedText": "ESTD", "ParentId": 0, "Type": "WORD", "Id": 2 }, { "Confidence": 91.49320983886719, "Geometry": { "BoundingBox": { "Width": 0.07007007300853729, "Top": 0.2828207015991211, "Left": 0.5675675868988037, "Height": 0.02250562608242035 }, "Polygon": [ { "Y": 0.2828207015991211, "X": 0.5675675868988037 }, { "Y": 0.2828207015991211, "X": 0.6376376152038574 }, { "Y": 0.30532634258270264, "X": 0.6376376152038574 }, { "Y": 0.30532634258270264, "X": 0.5675675868988037 } ] }, "DetectedText": "1882", "ParentId": 0, "Type": "WORD", "Id": 3 }, { "Confidence": 99.95779418945312, "Geometry": { "BoundingBox": { "Width": 0.33933934569358826, "Top": 0.32633158564567566, "Left": 0.3453453481197357, "Height": 0.07127484679222107 }, "Polygon": [ { "Y": 0.32633158564567566, "X": 0.3453453481197357 }, { "Y": 0.32633158564567566, "X": 0.684684693813324 }, { "Y": 0.39759939908981323, "X": 0.6836836934089661 }, { "Y": 0.39684921503067017, "X": 0.3453453481197357 } ] }, "DetectedText": "BRAINS", "ParentId": 1, "Type": "WORD", "Id": 4 } ] }`- 
                    For API details, see [DetectText](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/detect-text.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-celebrity-info`.

- **AWS CLI**
- 
            
                    **To get information about a celebrity**The following `get-celebrity-info`command displays information about the specified celebrity. The`id`parameter comes from a previous call to`recognize-celebrities`.`aws rekognition get-celebrity-info --id``nnnnnnn`Output: `{ "Name": "Celeb A", "Urls": [ "www.imdb.com/name/aaaaaaaaa" ] }`For more information, see [Getting Information About a Celebrity](https://docs.aws.amazon.com/rekognition/latest/dg/get-celebrity-info-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetCelebrityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-info.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-celebrity-recognition`.

- **AWS CLI**
- 
            
                    **To get the results of a celebrity recognition operation**The following `get-celebrity-recognition`command displays the results of a celebrity recognition operation that you started previously by calling`start-celebrity-recognition`.`aws rekognition get-celebrity-recognition \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "NextToken": "3D01ClxlCiT31VsRDkAO3IybLb/h5AtDWSGuhYi+N1FIJwwPtAkuKzDhL2rV3GcwmNt77+12", "Celebrities": [ { "Timestamp": 0, "Celebrity": { "Confidence": 96.0, "Face": { "BoundingBox": { "Width": 0.70333331823349, "Top": 0.16750000417232513, "Left": 0.19555555284023285, "Height": 0.3956249952316284 }, "Landmarks": [ { "Y": 0.31031012535095215, "X": 0.441436767578125, "Type": "eyeLeft" }, { "Y": 0.3081788718700409, "X": 0.6437258720397949, "Type": "eyeRight" }, { "Y": 0.39542075991630554, "X": 0.5572493076324463, "Type": "nose" }, { "Y": 0.4597957134246826, "X": 0.4579732120037079, "Type": "mouthLeft" }, { "Y": 0.45688048005104065, "X": 0.6349081993103027, "Type": "mouthRight" } ], "Pose": { "Yaw": 8.943398475646973, "Roll": -2.0309247970581055, "Pitch": -0.5674862861633301 }, "Quality": { "Sharpness": 99.40211486816406, "Brightness": 89.47132110595703 }, "Confidence": 99.99861145019531 }, "Name": "CelebrityA", "Urls": [ "www.imdb.com/name/111111111" ], "Id": "nnnnnn" } }, { "Timestamp": 467, "Celebrity": { "Confidence": 99.0, "Face": { "BoundingBox": { "Width": 0.6877777576446533, "Top": 0.18437500298023224, "Left": 0.20555555820465088, "Height": 0.3868750035762787 }, "Landmarks": [ { "Y": 0.31895750761032104, "X": 0.4411413371562958, "Type": "eyeLeft" }, { "Y": 0.3140959143638611, "X": 0.6523157954216003, "Type": "eyeRight" }, { "Y": 0.4016456604003906, "X": 0.5682755708694458, "Type": "nose" }, { "Y": 0.46894142031669617, "X": 0.4597797095775604, "Type": "mouthLeft" }, { "Y": 0.46971091628074646, "X": 0.6286435127258301, "Type": "mouthRight" } ], "Pose": { "Yaw": 10.433465957641602, "Roll": -3.347442388534546, "Pitch": 1.3709543943405151 }, "Quality": { "Sharpness": 99.5531005859375, "Brightness": 88.5764389038086 }, "Confidence": 99.99148559570312 }, "Name": "Jane Celebrity", "Urls": [ "www.imdb.com/name/111111111" ], "Id": "nnnnnn" } } ], "JobStatus": "SUCCEEDED", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.978118896484375, "Codec": "h264", "DurationMillis": 4570, "FrameHeight": 1920, "FrameWidth": 1080 } }`For more information, see [Recognizing Celebrities in a Stored Video](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-video-sqs.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetCelebrityRecognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-recognition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-content-moderation`.

- **AWS CLI**
- 
            
                    **To get the results of an unsafe content operation**The following `get-content-moderation`command displays the results of an unsafe content operation that you started previously by calling`start-content-moderation`.`aws rekognition get-content-moderation \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "NextToken": "dlhcKMHMzpCBGFukz6IO3JMcWiJAamCVhXHt3r6b4b5Tfbyw3q7o+Jeezt+ZpgfOnW9FCCgQ", "ModerationLabels": [ { "Timestamp": 0, "ModerationLabel": { "Confidence": 97.39583587646484, "ParentName": "", "Name": "Violence" } }, { "Timestamp": 0, "ModerationLabel": { "Confidence": 97.39583587646484, "ParentName": "Violence", "Name": "Weapon Violence" } } ], "JobStatus": "SUCCEEDED", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.97515869140625, "Codec": "h264", "DurationMillis": 6039, "FrameHeight": 1920, "FrameWidth": 1080 } }`For more information, see [Detecting Unsafe Stored Videos](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-videos.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetContentModeration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-content-moderation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-face-detection`.

- **AWS CLI**
- 
            
                    **To get the results of a face detection operation**The following `get-face-detection`command displays the results of a face detection operation that you started previously by calling`start-face-detection`.`aws rekognition get-face-detection \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "Faces": [ { "Timestamp": 467, "Face": { "BoundingBox": { "Width": 0.1560753583908081, "Top": 0.13555361330509186, "Left": -0.0952017530798912, "Height": 0.6934483051300049 }, "Landmarks": [ { "Y": 0.4013825058937073, "X": -0.041750285774469376, "Type": "eyeLeft" }, { "Y": 0.41695496439933777, "X": 0.027979329228401184, "Type": "eyeRight" }, { "Y": 0.6375303268432617, "X": -0.04034662991762161, "Type": "mouthLeft" }, { "Y": 0.6497718691825867, "X": 0.013960429467260838, "Type": "mouthRight" }, { "Y": 0.5238034129142761, "X": 0.008022055961191654, "Type": "nose" } ], "Pose": { "Yaw": -58.07863998413086, "Roll": 1.9384294748306274, "Pitch": -24.66305160522461 }, "Quality": { "Sharpness": 83.14741516113281, "Brightness": 25.75942611694336 }, "Confidence": 87.7622299194336 } }, { "Timestamp": 967, "Face": { "BoundingBox": { "Width": 0.28559377789497375, "Top": 0.19436298310756683, "Left": 0.024553587660193443, "Height": 0.7216082215309143 }, "Landmarks": [ { "Y": 0.4650231599807739, "X": 0.16269078850746155, "Type": "eyeLeft" }, { "Y": 0.4843238294124603, "X": 0.2782580852508545, "Type": "eyeRight" }, { "Y": 0.71530681848526, "X": 0.1741468608379364, "Type": "mouthLeft" }, { "Y": 0.7310671210289001, "X": 0.26857468485832214, "Type": "mouthRight" }, { "Y": 0.582602322101593, "X": 0.2566150426864624, "Type": "nose" } ], "Pose": { "Yaw": 11.487052917480469, "Roll": 5.074230670928955, "Pitch": 15.396159172058105 }, "Quality": { "Sharpness": 73.32209777832031, "Brightness": 54.96497344970703 }, "Confidence": 99.99998474121094 } } ], "NextToken": "OzL223pDKy9116O/02KXRqFIEAwxjy4PkgYcm3hSo0rdysbXg5Ex0eFgTGEj0ADEac6S037U", "JobStatus": "SUCCEEDED", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.970617294311523, "Codec": "h264", "DurationMillis": 6806, "FrameHeight": 1080, "FrameWidth": 1920 } }`For more information, see [Detecting Faces in a Stored Video](https://docs.aws.amazon.com/rekognition/latest/dg/faces-sqs-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetFaceDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-detection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-face-search`.

- **AWS CLI**
- 
            
                    **To get the results of a face search operation**The following `get-face-search`command displays the results of a face search operation that you started previously by calling`start-face-search`.`aws rekognition get-face-search \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "Persons": [ { "Timestamp": 467, "FaceMatches": [], "Person": { "Index": 0, "Face": { "BoundingBox": { "Width": 0.1560753583908081, "Top": 0.13555361330509186, "Left": -0.0952017530798912, "Height": 0.6934483051300049 }, "Landmarks": [ { "Y": 0.4013825058937073, "X": -0.041750285774469376, "Type": "eyeLeft" }, { "Y": 0.41695496439933777, "X": 0.027979329228401184, "Type": "eyeRight" }, { "Y": 0.6375303268432617, "X": -0.04034662991762161, "Type": "mouthLeft" }, { "Y": 0.6497718691825867, "X": 0.013960429467260838, "Type": "mouthRight" }, { "Y": 0.5238034129142761, "X": 0.008022055961191654, "Type": "nose" } ], "Pose": { "Yaw": -58.07863998413086, "Roll": 1.9384294748306274, "Pitch": -24.66305160522461 }, "Quality": { "Sharpness": 83.14741516113281, "Brightness": 25.75942611694336 }, "Confidence": 87.7622299194336 } } }, { "Timestamp": 967, "FaceMatches": [ { "Face": { "BoundingBox": { "Width": 0.12368900328874588, "Top": 0.16007399559020996, "Left": 0.5901259779930115, "Height": 0.2514039874076843 }, "FaceId": "056a95fa-2060-4159-9cab-7ed4daa030fa", "ExternalImageId": "image3.jpg", "Confidence": 100.0, "ImageId": "08f8a078-8929-37fd-8e8f-aadf690e8232" }, "Similarity": 98.44476318359375 } ], "Person": { "Index": 1, "Face": { "BoundingBox": { "Width": 0.28559377789497375, "Top": 0.19436298310756683, "Left": 0.024553587660193443, "Height": 0.7216082215309143 }, "Landmarks": [ { "Y": 0.4650231599807739, "X": 0.16269078850746155, "Type": "eyeLeft" }, { "Y": 0.4843238294124603, "X": 0.2782580852508545, "Type": "eyeRight" }, { "Y": 0.71530681848526, "X": 0.1741468608379364, "Type": "mouthLeft" }, { "Y": 0.7310671210289001, "X": 0.26857468485832214, "Type": "mouthRight" }, { "Y": 0.582602322101593, "X": 0.2566150426864624, "Type": "nose" } ], "Pose": { "Yaw": 11.487052917480469, "Roll": 5.074230670928955, "Pitch": 15.396159172058105 }, "Quality": { "Sharpness": 73.32209777832031, "Brightness": 54.96497344970703 }, "Confidence": 99.99998474121094 } } } ], "NextToken": "5bkgcezyuaqhtWk3C8OTW6cjRghrwV9XDMivm5B3MXm+Lv6G+L+GejyFHPhoNa/ldXIC4c/d", "JobStatus": "SUCCEEDED", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.970617294311523, "Codec": "h264", "DurationMillis": 6806, "FrameHeight": 1080, "FrameWidth": 1920 } }`For more information, see [Searching Stored Videos for Faces](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetFaceSearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-face-search.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-label-detection`.

- **AWS CLI**
- 
            
                    **To get the results of an objects and scenes detection operation**The following `get-label-detection`command displays the results of an objects and scenes detection operation that you started previously by calling`start-label-detection`.`aws rekognition get-label-detection \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "Labels": [ { "Timestamp": 0, "Label": { "Instances": [], "Confidence": 50.19071578979492, "Parents": [ { "Name": "Person" }, { "Name": "Crowd" } ], "Name": "Audience" } }, { "Timestamp": 0, "Label": { "Instances": [], "Confidence": 55.74115753173828, "Parents": [ { "Name": "Room" }, { "Name": "Indoors" }, { "Name": "School" } ], "Name": "Classroom" } } ], "JobStatus": "SUCCEEDED", "LabelModelVersion": "2.0", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.970617294311523, "Codec": "h264", "DurationMillis": 6806, "FrameHeight": 1080, "FrameWidth": 1920 }, "NextToken": "BMugzAi4L72IERzQdbpyMQuEFBsjlo5W0Yx3mfG+sR9mm98E1/CpObenspRfs/5FBQFs4X7G" }`For more information, see [Detecting Labels in a Video](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetLabelDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-label-detection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-person-tracking`.

- **AWS CLI**
- 
            
                    **To get the results of a people pathing operation**The following `get-person-tracking`command displays the results of a people pathing operation that you started previously by calling`start-person-tracking`.`aws rekognition get-person-tracking \ --job-id``1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef`Output: `{ "Persons": [ { "Timestamp": 500, "Person": { "BoundingBox": { "Width": 0.4151041805744171, "Top": 0.07870370149612427, "Left": 0.0, "Height": 0.9212962985038757 }, "Index": 0 } }, { "Timestamp": 567, "Person": { "BoundingBox": { "Width": 0.4755208194255829, "Top": 0.07777778059244156, "Left": 0.0, "Height": 0.9194444417953491 }, "Index": 0 } } ], "NextToken": "D/vRIYNyhG79ugdta3f+8cRg9oSRo+HigGOuxRiYpTn0ExnqTi1CJektVAc4HrAXDv25eHYk", "JobStatus": "SUCCEEDED", "VideoMetadata": { "Format": "QuickTime / MOV", "FrameRate": 29.970617294311523, "Codec": "h264", "DurationMillis": 6806, "FrameHeight": 1080, "FrameWidth": 1920 } }`For more information, see [People Pathing](https://docs.aws.amazon.com/rekognition/latest/dg/persons.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [GetPersonTracking](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-person-tracking.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `index-faces`.

For more information, see [Adding faces to a collection](https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To add faces to a collection**The following `index-faces`command adds the faces found in an image to the specified collection.`aws rekognition index-faces \ --image '``{"S3Object":{"Bucket":"MyVideoS3Bucket","Name":"MyPicture.jpg"}}`' \ --collection-id`MyCollection`\ --max-faces`1`\ --quality-filter`"AUTO"`\ --detection-attributes`"ALL"`\ --external-image-id`"MyPicture.jpg"`Output: `{ "FaceRecords": [ { "FaceDetail": { "Confidence": 99.993408203125, "Eyeglasses": { "Confidence": 99.11750030517578, "Value": false }, "Sunglasses": { "Confidence": 99.98249053955078, "Value": false }, "Gender": { "Confidence": 99.92769622802734, "Value": "Male" }, "Landmarks": [ { "Y": 0.26750367879867554, "X": 0.6202793717384338, "Type": "eyeLeft" }, { "Y": 0.26642778515815735, "X": 0.6787431836128235, "Type": "eyeRight" }, { "Y": 0.31361380219459534, "X": 0.6421601176261902, "Type": "nose" }, { "Y": 0.3495299220085144, "X": 0.6216195225715637, "Type": "mouthLeft" }, { "Y": 0.35194727778434753, "X": 0.669899046421051, "Type": "mouthRight" }, { "Y": 0.26844894886016846, "X": 0.6210268139839172, "Type": "leftPupil" }, { "Y": 0.26707562804222107, "X": 0.6817160844802856, "Type": "rightPupil" }, { "Y": 0.24834522604942322, "X": 0.6018546223640442, "Type": "leftEyeBrowLeft" }, { "Y": 0.24397172033786774, "X": 0.6172008514404297, "Type": "leftEyeBrowUp" }, { "Y": 0.24677404761314392, "X": 0.6339119076728821, "Type": "leftEyeBrowRight" }, { "Y": 0.24582654237747192, "X": 0.6619398593902588, "Type": "rightEyeBrowLeft" }, { "Y": 0.23973053693771362, "X": 0.6804757118225098, "Type": "rightEyeBrowUp" }, { "Y": 0.24441994726657867, "X": 0.6978968977928162, "Type": "rightEyeBrowRight" }, { "Y": 0.2695908546447754, "X": 0.6085202693939209, "Type": "leftEyeLeft" }, { "Y": 0.26716896891593933, "X": 0.6315826177597046, "Type": "leftEyeRight" }, { "Y": 0.26289820671081543, "X": 0.6202316880226135, "Type": "leftEyeUp" }, { "Y": 0.27123287320137024, "X": 0.6205548048019409, "Type": "leftEyeDown" }, { "Y": 0.2668408751487732, "X": 0.6663622260093689, "Type": "rightEyeLeft" }, { "Y": 0.26741549372673035, "X": 0.6910083889961243, "Type": "rightEyeRight" }, { "Y": 0.2614026665687561, "X": 0.6785826086997986, "Type": "rightEyeUp" }, { "Y": 0.27075251936912537, "X": 0.6789616942405701, "Type": "rightEyeDown" }, { "Y": 0.3211299479007721, "X": 0.6324167847633362, "Type": "noseLeft" }, { "Y": 0.32276326417922974, "X": 0.6558475494384766, "Type": "noseRight" }, { "Y": 0.34385165572166443, "X": 0.6444970965385437, "Type": "mouthUp" }, { "Y": 0.3671635091304779, "X": 0.6459195017814636, "Type": "mouthDown" } ], "Pose": { "Yaw": -9.54541015625, "Roll": -0.5709401965141296, "Pitch": 0.6045494675636292 }, "Emotions": [ { "Confidence": 39.90074157714844, "Type": "HAPPY" }, { "Confidence": 23.38753890991211, "Type": "CALM" }, { "Confidence": 5.840933322906494, "Type": "CONFUSED" } ], "AgeRange": { "High": 63, "Low": 45 }, "EyesOpen": { "Confidence": 99.80887603759766, "Value": true }, "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618015021085739, "Left": 0.5575000047683716, "Height": 0.24770642817020416 }, "Smile": { "Confidence": 99.69740295410156, "Value": false }, "MouthOpen": { "Confidence": 99.97393798828125, "Value": false }, "Quality": { "Sharpness": 95.54405975341797, "Brightness": 63.867706298828125 }, "Mustache": { "Confidence": 97.05007934570312, "Value": false }, "Beard": { "Confidence": 87.34505462646484, "Value": false } }, "Face": { "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618015021085739, "Left": 0.5575000047683716, "Height": 0.24770642817020416 }, "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f", "ExternalImageId": "example-image.jpg", "Confidence": 99.993408203125, "ImageId": "8d67061e-90d2-598f-9fbd-29c8497039c0" } } ], "UnindexedFaces": [], "FaceModelVersion": "3.0", "OrientationCorrection": "ROTATE_0" }`For more information, see [Adding Faces to a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [IndexFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-collections`.

For more information, see [Listing collections](https://docs.aws.amazon.com/rekognition/latest/dg/list-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To list the available collections**The following `list-collections`command lists the available collections in the AWS account.`aws rekognition list-collections`Output: `{ "FaceModelVersions": [ "2.0", "3.0", "3.0", "3.0", "4.0", "1.0", "3.0", "4.0", "4.0", "4.0" ], "CollectionIds": [ "MyCollection1", "MyCollection2", "MyCollection3", "MyCollection4", "MyCollection5", "MyCollection6", "MyCollection7", "MyCollection8", "MyCollection9", "MyCollection10" ] }`For more information, see [Listing Collections](https://docs.aws.amazon.com/rekognition/latest/dg/list-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [ListCollections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-collections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-faces`.

For more information, see [Listing faces in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/list-faces-in-collection-procedure.html).

- **AWS CLI**
- 
            
                    **To list the faces in a collection**The following `list-faces`command lists the faces in the specified collection.`aws rekognition list-faces \ --collection-id``MyCollection`Output: `{ "FaceModelVersion": "3.0", "Faces": [ { "BoundingBox": { "Width": 0.5216310024261475, "Top": 0.3256250023841858, "Left": 0.13394300639629364, "Height": 0.3918749988079071 }, "FaceId": "0040279c-0178-436e-b70a-e61b074e96b0", "ExternalImageId": "image1.jpg", "Confidence": 100.0, "ImageId": "f976e487-3719-5e2d-be8b-ea2724c26991" }, { "BoundingBox": { "Width": 0.5074880123138428, "Top": 0.3774999976158142, "Left": 0.18302799761295319, "Height": 0.3812499940395355 }, "FaceId": "086261e8-6deb-4bc0-ac73-ab22323cc38d", "ExternalImageId": "image2.jpg", "Confidence": 99.99930572509766, "ImageId": "ae1593b0-a8f6-5e24-a306-abf529e276fa" }, { "BoundingBox": { "Width": 0.5574039816856384, "Top": 0.37187498807907104, "Left": 0.14559100568294525, "Height": 0.4181250035762787 }, "FaceId": "11c4bd3c-19c5-4eb8-aecc-24feb93a26e1", "ExternalImageId": "image3.jpg", "Confidence": 99.99960327148438, "ImageId": "80739b4d-883f-5b78-97cf-5124038e26b9" }, { "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618019938468933, "Left": 0.5575000047683716, "Height": 0.24770599603652954 }, "FaceId": "13692fe4-990a-4679-b14a-5ac23d135eab", "ExternalImageId": "image4.jpg", "Confidence": 99.99340057373047, "ImageId": "8df18239-9ad1-5acd-a46a-6581ff98f51b" }, { "BoundingBox": { "Width": 0.5307819843292236, "Top": 0.2862499952316284, "Left": 0.1564060002565384, "Height": 0.3987500071525574 }, "FaceId": "2eb5f3fd-e2a9-4b1c-a89f-afa0a518fe06", "ExternalImageId": "image5.jpg", "Confidence": 99.99970245361328, "ImageId": "3c314792-197d-528d-bbb6-798ed012c150" }, { "BoundingBox": { "Width": 0.5773710012435913, "Top": 0.34437501430511475, "Left": 0.12396000325679779, "Height": 0.4337500035762787 }, "FaceId": "57189455-42b0-4839-a86c-abda48b13174", "ExternalImageId": "image6.jpg", "Confidence": 100.0, "ImageId": "0aff2f37-e7a2-5dbc-a3a3-4ef6ec18eaa0" }, { "BoundingBox": { "Width": 0.5349419713020325, "Top": 0.29124999046325684, "Left": 0.16389399766921997, "Height": 0.40187498927116394 }, "FaceId": "745f7509-b1fa-44e0-8b95-367b1359638a", "ExternalImageId": "image7.jpg", "Confidence": 99.99979400634766, "ImageId": "67a34327-48d1-5179-b042-01e52ccfeada" }, { "BoundingBox": { "Width": 0.41499999165534973, "Top": 0.09187500178813934, "Left": 0.28083300590515137, "Height": 0.3112500011920929 }, "FaceId": "8d3cfc70-4ba8-4b36-9644-90fba29c2dac", "ExternalImageId": "image8.jpg", "Confidence": 99.99769592285156, "ImageId": "a294da46-2cb1-5cc4-9045-61d7ca567662" }, { "BoundingBox": { "Width": 0.48166701197624207, "Top": 0.20999999344348907, "Left": 0.21250000596046448, "Height": 0.36125001311302185 }, "FaceId": "bd4ceb4d-9acc-4ab7-8ef8-1c2d2ba0a66a", "ExternalImageId": "image9.jpg", "Confidence": 99.99949645996094, "ImageId": "5e1a7588-e5a0-5ee3-bd00-c642518dfe3a" }, { "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618019938468933, "Left": 0.5575000047683716, "Height": 0.24770599603652954 }, "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f", "ExternalImageId": "image10.jpg", "Confidence": 99.99340057373047, "ImageId": "8d67061e-90d2-598f-9fbd-29c8497039c0" } ] }`For more information, see [Listing Faces in a Collection](https://docs.aws.amazon.com/rekognition/latest/dg/list-faces-in-collection-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [ListFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stream-processors`.

- **AWS CLI**
- 
            
                    **To list the stream processors in your account**The following `list-stream-processors`command lists the stream processors in your account and the state of each.`aws rekognition list-stream-processors`Output: `{ "StreamProcessors": [ { "Status": "STOPPED", "Name": "my-stream-processor" } ] }`For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [ListStreamProcessors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/list-stream-processors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `recognize-celebrities`.

For more information, see [Recognizing celebrities in an image](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-procedure-image.html).

- **AWS CLI**
- 
            
                    **To recognize celebrities in an image**The following `recognize-celebrities`command recognizes celebrities in the specified image stored in an Amazon S3 bucket.:`aws rekognition recognize-celebrities \ --image``"S3Object={Bucket=MyImageS3Bucket,Name=moviestars.jpg}"`Output: `{ "UnrecognizedFaces": [ { "BoundingBox": { "Width": 0.14416666328907013, "Top": 0.07777778059244156, "Left": 0.625, "Height": 0.2746031880378723 }, "Confidence": 99.9990234375, "Pose": { "Yaw": 10.80408763885498, "Roll": -12.761146545410156, "Pitch": 10.96889877319336 }, "Quality": { "Sharpness": 94.1185531616211, "Brightness": 79.18367004394531 }, "Landmarks": [ { "Y": 0.18220913410186768, "X": 0.6702951788902283, "Type": "eyeLeft" }, { "Y": 0.16337193548679352, "X": 0.7188183665275574, "Type": "eyeRight" }, { "Y": 0.20739148557186127, "X": 0.7055801749229431, "Type": "nose" }, { "Y": 0.2889308035373688, "X": 0.687512218952179, "Type": "mouthLeft" }, { "Y": 0.2706988751888275, "X": 0.7250053286552429, "Type": "mouthRight" } ] } ], "CelebrityFaces": [ { "MatchConfidence": 100.0, "Face": { "BoundingBox": { "Width": 0.14000000059604645, "Top": 0.1190476194024086, "Left": 0.82833331823349, "Height": 0.2666666805744171 }, "Confidence": 99.99359130859375, "Pose": { "Yaw": -10.509642601013184, "Roll": -14.51749324798584, "Pitch": 13.799399375915527 }, "Quality": { "Sharpness": 78.74752044677734, "Brightness": 42.201324462890625 }, "Landmarks": [ { "Y": 0.2290833294391632, "X": 0.8709492087364197, "Type": "eyeLeft" }, { "Y": 0.20639978349208832, "X": 0.9153988361358643, "Type": "eyeRight" }, { "Y": 0.25417643785476685, "X": 0.8907724022865295, "Type": "nose" }, { "Y": 0.32729196548461914, "X": 0.8876466155052185, "Type": "mouthLeft" }, { "Y": 0.3115464746952057, "X": 0.9238573312759399, "Type": "mouthRight" } ] }, "Name": "Celeb A", "Urls": [ "www.imdb.com/name/aaaaaaaaa" ], "Id": "1111111" }, { "MatchConfidence": 97.0, "Face": { "BoundingBox": { "Width": 0.13333334028720856, "Top": 0.24920634925365448, "Left": 0.4449999928474426, "Height": 0.2539682686328888 }, "Confidence": 99.99979400634766, "Pose": { "Yaw": 6.557040691375732, "Roll": -7.316643714904785, "Pitch": 9.272967338562012 }, "Quality": { "Sharpness": 83.23492431640625, "Brightness": 78.83267974853516 }, "Landmarks": [ { "Y": 0.3625510632991791, "X": 0.48898839950561523, "Type": "eyeLeft" }, { "Y": 0.35366007685661316, "X": 0.5313721299171448, "Type": "eyeRight" }, { "Y": 0.3894785940647125, "X": 0.5173314809799194, "Type": "nose" }, { "Y": 0.44889405369758606, "X": 0.5020005702972412, "Type": "mouthLeft" }, { "Y": 0.4408611059188843, "X": 0.5351271629333496, "Type": "mouthRight" } ] }, "Name": "Celeb B", "Urls": [ "www.imdb.com/name/bbbbbbbbb" ], "Id": "2222222" }, { "MatchConfidence": 100.0, "Face": { "BoundingBox": { "Width": 0.12416666746139526, "Top": 0.2968254089355469, "Left": 0.2150000035762787, "Height": 0.23650793731212616 }, "Confidence": 99.99958801269531, "Pose": { "Yaw": 7.801797866821289, "Roll": -8.326810836791992, "Pitch": 7.844768047332764 }, "Quality": { "Sharpness": 86.93206024169922, "Brightness": 79.81291198730469 }, "Landmarks": [ { "Y": 0.4027804136276245, "X": 0.2575301229953766, "Type": "eyeLeft" }, { "Y": 0.3934555947780609, "X": 0.2956969439983368, "Type": "eyeRight" }, { "Y": 0.4309830069541931, "X": 0.2837020754814148, "Type": "nose" }, { "Y": 0.48186683654785156, "X": 0.26812544465065, "Type": "mouthLeft" }, { "Y": 0.47338807582855225, "X": 0.29905644059181213, "Type": "mouthRight" } ] }, "Name": "Celeb C", "Urls": [ "www.imdb.com/name/ccccccccc" ], "Id": "3333333" }, { "MatchConfidence": 97.0, "Face": { "BoundingBox": { "Width": 0.11916666477918625, "Top": 0.3698412775993347, "Left": 0.008333333767950535, "Height": 0.22698412835597992 }, "Confidence": 99.99999237060547, "Pose": { "Yaw": 16.38478660583496, "Roll": -1.0260354280471802, "Pitch": 5.975185394287109 }, "Quality": { "Sharpness": 83.23492431640625, "Brightness": 61.408443450927734 }, "Landmarks": [ { "Y": 0.4632347822189331, "X": 0.049406956881284714, "Type": "eyeLeft" }, { "Y": 0.46388113498687744, "X": 0.08722897619009018, "Type": "eyeRight" }, { "Y": 0.5020678639411926, "X": 0.0758260041475296, "Type": "nose" }, { "Y": 0.544157862663269, "X": 0.054029736667871475, "Type": "mouthLeft" }, { "Y": 0.5463630557060242, "X": 0.08464983850717545, "Type": "mouthRight" } ] }, "Name": "Celeb D", "Urls": [ "www.imdb.com/name/ddddddddd" ], "Id": "4444444" } ] }`For more information, see [Recognizing Celebrities in an Image](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-procedure-image.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [RecognizeCelebrities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/recognize-celebrities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-faces-by-image`.

For more information, see [Searching for a face (image)](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-image-procedure.html).

- **AWS CLI**
- 
            
                    **To search for faces in a collection that match the largest face in an image.**The following `search-faces-by-image`command searches for faces in a collection that match the largest face in the specified image.:`aws rekognition search-faces-by-image \ --image '``{"S3Object":{"Bucket":"MyImageS3Bucket","Name":"ExamplePerson.jpg"}}`' \ --collection-id`MyFaceImageCollection``{`"SearchedFaceBoundingBox":`{`"Width":`0.18562500178813934,`"Top":`0.1618015021085739,`"Left":`0.5575000047683716,`"Height":`0.24770642817020416``},`"SearchedFaceConfidence":`99.993408203125,`"FaceMatches":`[``{`"Face":`{`"BoundingBox":`{`"Width":`0.18562500178813934,`"Top":`0.1618019938468933,`"Left":`0.5575000047683716,`"Height":`0.24770599603652954``},`"FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f", "ExternalImageId": "example-image.jpg", "Confidence":`99.99340057373047,`"ImageId":`"8d67061e-90d2-598f-9fbd-29c8497039c0"``},`"Similarity":`99.97913360595703``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.18562500178813934,`"Top":`0.1618019938468933,`"Left":`0.5575000047683716,`"Height":`0.24770599603652954``},`"FaceId": "13692fe4-990a-4679-b14a-5ac23d135eab", "ExternalImageId": "image3.jpg", "Confidence":`99.99340057373047,`"ImageId":`"8df18239-9ad1-5acd-a46a-6581ff98f51b"``},`"Similarity":`99.97913360595703``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.41499999165534973,`"Top":`0.09187500178813934,`"Left":`0.28083300590515137,`"Height":`0.3112500011920929``},`"FaceId": "8d3cfc70-4ba8-4b36-9644-90fba29c2dac", "ExternalImageId": "image2.jpg", "Confidence":`99.99769592285156,`"ImageId":`"a294da46-2cb1-5cc4-9045-61d7ca567662"``},`"Similarity":`99.18069458007812``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.48166701197624207,`"Top":`0.20999999344348907,`"Left":`0.21250000596046448,`"Height":`0.36125001311302185``},`"FaceId": "bd4ceb4d-9acc-4ab7-8ef8-1c2d2ba0a66a", "ExternalImageId": "image1.jpg", "Confidence":`99.99949645996094,`"ImageId":`"5e1a7588-e5a0-5ee3-bd00-c642518dfe3a"``},`"Similarity":`98.66607666015625``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.5349419713020325,`"Top":`0.29124999046325684,`"Left":`0.16389399766921997,`"Height":`0.40187498927116394``},`"FaceId": "745f7509-b1fa-44e0-8b95-367b1359638a", "ExternalImageId": "image9.jpg", "Confidence":`99.99979400634766,`"ImageId":`"67a34327-48d1-5179-b042-01e52ccfeada"``},`"Similarity":`98.24278259277344``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.5307819843292236,`"Top":`0.2862499952316284,`"Left":`0.1564060002565384,`"Height":`0.3987500071525574``},`"FaceId": "2eb5f3fd-e2a9-4b1c-a89f-afa0a518fe06", "ExternalImageId": "image10.jpg", "Confidence":`99.99970245361328,`"ImageId":`"3c314792-197d-528d-bbb6-798ed012c150"``},`"Similarity":`98.10665893554688``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.5074880123138428,`"Top":`0.3774999976158142,`"Left":`0.18302799761295319,`"Height":`0.3812499940395355``},`"FaceId": "086261e8-6deb-4bc0-ac73-ab22323cc38d", "ExternalImageId": "image6.jpg", "Confidence":`99.99930572509766,`"ImageId":`"ae1593b0-a8f6-5e24-a306-abf529e276fa"``},`"Similarity":`98.10526275634766``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.5574039816856384,`"Top":`0.37187498807907104,`"Left":`0.14559100568294525,`"Height":`0.4181250035762787``},`"FaceId": "11c4bd3c-19c5-4eb8-aecc-24feb93a26e1", "ExternalImageId": "image5.jpg", "Confidence":`99.99960327148438,`"ImageId":`"80739b4d-883f-5b78-97cf-5124038e26b9"``},`"Similarity":`97.94659423828125``},``{`"Face":`{`"BoundingBox":`{`"Width":`0.5773710012435913,`"Top":`0.34437501430511475,`"Left":`0.12396000325679779,`"Height":`0.4337500035762787``},`"FaceId": "57189455-42b0-4839-a86c-abda48b13174", "ExternalImageId": "image8.jpg", "Confidence":`100.0,`"ImageId":`"0aff2f37-e7a2-5dbc-a3a3-4ef6ec18eaa0"``},`"Similarity":`97.93476867675781``}``],`"FaceModelVersion":`"3.0"``}`For more information, see [Searching for a Face Using an Image](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-image-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [SearchFacesByImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces-by-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-faces`.

For more information, see [Searching for a face (face ID)](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-id-procedure.html).

- **AWS CLI**
- 
            
                    **To search for faces in a collection that match a face ID.**The following `search-faces`command searches for faces in a collection that match the specified face ID.`aws rekognition search-faces \ --face-id``8d3cfc70-4ba8-4b36-9644-90fba29c2dac`\ --collection-id`MyCollection`Output: `{ "SearchedFaceId": "8d3cfc70-4ba8-4b36-9644-90fba29c2dac", "FaceModelVersion": "3.0", "FaceMatches": [ { "Face": { "BoundingBox": { "Width": 0.48166701197624207, "Top": 0.20999999344348907, "Left": 0.21250000596046448, "Height": 0.36125001311302185 }, "FaceId": "bd4ceb4d-9acc-4ab7-8ef8-1c2d2ba0a66a", "ExternalImageId": "image1.jpg", "Confidence": 99.99949645996094, "ImageId": "5e1a7588-e5a0-5ee3-bd00-c642518dfe3a" }, "Similarity": 99.30997467041016 }, { "Face": { "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618019938468933, "Left": 0.5575000047683716, "Height": 0.24770599603652954 }, "FaceId": "ce7ed422-2132-4a11-ab14-06c5c410f29f", "ExternalImageId": "example-image.jpg", "Confidence": 99.99340057373047, "ImageId": "8d67061e-90d2-598f-9fbd-29c8497039c0" }, "Similarity": 99.24862670898438 }, { "Face": { "BoundingBox": { "Width": 0.18562500178813934, "Top": 0.1618019938468933, "Left": 0.5575000047683716, "Height": 0.24770599603652954 }, "FaceId": "13692fe4-990a-4679-b14a-5ac23d135eab", "ExternalImageId": "image3.jpg", "Confidence": 99.99340057373047, "ImageId": "8df18239-9ad1-5acd-a46a-6581ff98f51b" }, "Similarity": 99.24862670898438 }, { "Face": { "BoundingBox": { "Width": 0.5349419713020325, "Top": 0.29124999046325684, "Left": 0.16389399766921997, "Height": 0.40187498927116394 }, "FaceId": "745f7509-b1fa-44e0-8b95-367b1359638a", "ExternalImageId": "image9.jpg", "Confidence": 99.99979400634766, "ImageId": "67a34327-48d1-5179-b042-01e52ccfeada" }, "Similarity": 96.73158264160156 }, { "Face": { "BoundingBox": { "Width": 0.5307819843292236, "Top": 0.2862499952316284, "Left": 0.1564060002565384, "Height": 0.3987500071525574 }, "FaceId": "2eb5f3fd-e2a9-4b1c-a89f-afa0a518fe06", "ExternalImageId": "image10.jpg", "Confidence": 99.99970245361328, "ImageId": "3c314792-197d-528d-bbb6-798ed012c150" }, "Similarity": 96.48291015625 }, { "Face": { "BoundingBox": { "Width": 0.5074880123138428, "Top": 0.3774999976158142, "Left": 0.18302799761295319, "Height": 0.3812499940395355 }, "FaceId": "086261e8-6deb-4bc0-ac73-ab22323cc38d", "ExternalImageId": "image6.jpg", "Confidence": 99.99930572509766, "ImageId": "ae1593b0-a8f6-5e24-a306-abf529e276fa" }, "Similarity": 96.43287658691406 }, { "Face": { "BoundingBox": { "Width": 0.5574039816856384, "Top": 0.37187498807907104, "Left": 0.14559100568294525, "Height": 0.4181250035762787 }, "FaceId": "11c4bd3c-19c5-4eb8-aecc-24feb93a26e1", "ExternalImageId": "image5.jpg", "Confidence": 99.99960327148438, "ImageId": "80739b4d-883f-5b78-97cf-5124038e26b9" }, "Similarity": 95.25305938720703 }, { "Face": { "BoundingBox": { "Width": 0.5773710012435913, "Top": 0.34437501430511475, "Left": 0.12396000325679779, "Height": 0.4337500035762787 }, "FaceId": "57189455-42b0-4839-a86c-abda48b13174", "ExternalImageId": "image8.jpg", "Confidence": 100.0, "ImageId": "0aff2f37-e7a2-5dbc-a3a3-4ef6ec18eaa0" }, "Similarity": 95.22837829589844 } ] }`For more information, see [Searching for a Face Using Its Face ID](https://docs.aws.amazon.com/rekognition/latest/dg/search-face-with-id-procedure.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [SearchFaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/search-faces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-celebrity-recognition`.

- **AWS CLI**
- 
            
                    **To start the recognition of celebrities in a stored video**The following `start-celebrity-recognition`command starts a job to look for celebrities in the specified video file stored in an Amazon S3 bucket.`aws rekognition start-celebrity-recognition \ --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`Output: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [Recognizing Celebrities in a Stored Video](https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-video-sqs.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartCelebrityRecognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-celebrity-recognition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-content-moderation`.

- **AWS CLI**
- 
            
                    **To start the recognition of unsafe content in a stored video**The following `start-content-moderation`command starts a job to detect unsafe content in the specified video file stored in an Amazon S3 bucket.`aws rekognition start-content-moderation \ --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`Output: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [Detecting Unsafe Stored Videos](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-moderate-videos.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartContentModeration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-content-moderation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-face-detection`.

- **AWS CLI**
- 
            
                    **To detect faces in a video**The following `start-face-detection`command starts a job to detect faces in the specified video file stored in an Amazon S3 bucket.`aws rekognition start-face-detection --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`Output: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [Detecting Faces in a Stored Video](https://docs.aws.amazon.com/rekognition/latest/dg/faces-sqs-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartFaceDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-face-detection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-face-search`.

- **AWS CLI**
- 
            
                    **To search for faces in a collection that match faces detected in a video**The following `start-face-search`command starts a job to search for faces in a collection that match faces detected in the specified video file in an Amazon S3 bucket.`aws rekognition start-face-search \ --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`\ --`collection`-id collectionOutput: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [Searching Stored Videos for Faces](https://docs.aws.amazon.com/rekognition/latest/dg/procedure-person-search-videos.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartFaceSearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-face-search.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-label-detection`.

- **AWS CLI**
- 
            
                    **To detect objects and scenes in a video**The following `start-label-detection`command starts a job to detect objects and scenes in the specified video file stored in an Amazon S3 bucket.`aws rekognition start-label-detection \ --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`Output: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [Detecting Labels in a Video](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detecting-labels-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartLabelDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-label-detection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-person-tracking`.

- **AWS CLI**
- 
            
                    **To start the pathing of people in a stored video**The following `start-person-tracking`command starts a job to track the paths that people take in the specified video fiel stored in an Amazon S3 bucket.:`aws rekognition start-person-tracking \ --video``"S3Object={Bucket=MyVideoS3Bucket,Name=MyVideoFile.mpg}"`Output: `{ "JobId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef" }`For more information, see [People Pathing](https://docs.aws.amazon.com/rekognition/latest/dg/persons.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartPersonTracking](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-person-tracking.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-stream-processor`.

- **AWS CLI**
- 
            
                    **To start a stream processor**The following `start-stream-processor`command starts the specified video stream processor.`aws rekognition start-stream-processor \ --name``my-stream-processor`This command produces no output. For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StartStreamProcessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-stream-processor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-stream-processor`.

- **AWS CLI**
- 
            
                    **To stop a running stream processor**The following `stop-stream-processor`command stops the specified running stream processor.`aws rekognition stop-stream-processor \ --name``my-stream-processor`This command produces no output. For more information, see [Working with Streaming Videos](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)in the*Amazon Rekognition Developer Guide*.- 
                    For API details, see [StopStreamProcessor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/stop-stream-processor.html)in*AWS CLI Command Reference*.
 
-