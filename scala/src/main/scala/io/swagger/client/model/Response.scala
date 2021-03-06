/**
 * GraphHopper Directions API
 * You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model


case class Response (
  copyrights: Option[List[String]] = None,
  // unique identify of job - which you get when posting your request to the large problem solver
  jobId: Option[String] = None,
  // indicates the current status of the job
  status: Option[String] = None,
  // waiting time in ms
  waitingTimeInQueue: Option[Long] = None,
  // processing time in ms. if job is still waiting in queue, processing_time is 0
  processingTime: Option[Long] = None,
  // the solution. only available if status field indicates finished
  solution: Option[Solution] = None
)

