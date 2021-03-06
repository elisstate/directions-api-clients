# SWGVehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vehicleId** | **NSString*** | Unique identifier of vehicle | [optional] 
**typeId** | **NSString*** | Unique identifier referring to the available vehicle types | [optional] 
**startAddress** | [**SWGAddress***](SWGAddress.md) |  | [optional] 
**endAddress** | [**SWGAddress***](SWGAddress.md) |  | [optional] 
**_break** | [**SWGBreak***](SWGBreak.md) |  | [optional] 
**returnToDepot** | **NSNumber*** | Indicates whether vehicle should return to start address or not. If not, it can end at any service activity. | [optional] 
**earliestStart** | **NSNumber*** | earliest start of vehicle at its start location | [optional] 
**latestEnd** | **NSNumber*** | latest end of vehicle at its end location | [optional] 
**skills** | **NSArray&lt;NSString*&gt;*** | array of skills | [optional] 
**maxDistance** | **NSNumber*** | max distance of vehicle | [optional] 
**maxDrivingTime** | **NSNumber*** | max drive time of vehicle | [optional] 
**maxJobs** | **NSNumber*** | max number of jobs the vehicle can load | [optional] 
**maxActivities** | **NSNumber*** | max number of activities the vehicle can conduct | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


