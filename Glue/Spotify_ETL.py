import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Track
Track_node1751395434744 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bb-spotify-project-1/staging/track.csv"], "recurse": True}, transformation_ctx="Track_node1751395434744")

# Script generated for node Artist
Artist_node1751395427736 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bb-spotify-project-1/staging/artists.csv"], "recurse": True}, transformation_ctx="Artist_node1751395427736")

# Script generated for node Albums
Albums_node1751395434176 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bb-spotify-project-1/staging/albums.csv"], "recurse": True}, transformation_ctx="Albums_node1751395434176")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1751395984867 = Join.apply(frame1=Artist_node1751395427736, frame2=Albums_node1751395434176, keys1=["id"], keys2=["artist_id"], transformation_ctx="JoinAlbumArtist_node1751395984867")

# Script generated for node Join with Tracks
JoinwithTracks_node1751396085503 = Join.apply(frame1=JoinAlbumArtist_node1751395984867, frame2=Track_node1751395434744, keys1=["track_id"], keys2=["track_id"], transformation_ctx="JoinwithTracks_node1751396085503")

# Script generated for node Drop Fields
DropFields_node1751396139085 = DropFields.apply(frame=JoinwithTracks_node1751396085503, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1751396139085")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1751396139085, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1751395370230", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1751396197499 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1751396139085, connection_type="s3", format="glueparquet", connection_options={"path": "s3://bb-spotify-project-1/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1751396197499")

job.commit()