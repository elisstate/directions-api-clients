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


#include "SWGResponseInfo.h"

#include "SWGHelpers.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QObject>
#include <QDebug>

namespace Swagger {


SWGResponseInfo::SWGResponseInfo(QString* json) {
    init();
    this->fromJson(*json);
}

SWGResponseInfo::SWGResponseInfo() {
    init();
}

SWGResponseInfo::~SWGResponseInfo() {
    this->cleanup();
}

void
SWGResponseInfo::init() {
    copyrights = new QList<QString*>();
    took = 0.0;
}

void
SWGResponseInfo::cleanup() {
    
    if(copyrights != nullptr) {
        QList<QString*>* arr = copyrights;
        foreach(QString* o, *arr) {
            delete o;
        }
        delete copyrights;
    }

}

SWGResponseInfo*
SWGResponseInfo::fromJson(QString &json) {
    QByteArray array (json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
    return this;
}

void
SWGResponseInfo::fromJsonObject(QJsonObject &pJson) {
    
    ::Swagger::setValue(&copyrights, pJson["copyrights"], "QList", "QString");
    
    ::Swagger::setValue(&took, pJson["took"], "double", "");
}

QString
SWGResponseInfo::asJson ()
{
    QJsonObject* obj = this->asJsonObject();
    
    QJsonDocument doc(*obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject*
SWGResponseInfo::asJsonObject() {
    QJsonObject* obj = new QJsonObject();
    
    QJsonArray copyrightsJsonArray;
    toJsonArray((QList<void*>*)copyrights, &copyrightsJsonArray, "copyrights", "QString");
    obj->insert("copyrights", copyrightsJsonArray);

    obj->insert("took", QJsonValue(took));

    return obj;
}

QList<QString*>*
SWGResponseInfo::getCopyrights() {
    return copyrights;
}
void
SWGResponseInfo::setCopyrights(QList<QString*>* copyrights) {
    this->copyrights = copyrights;
}

double
SWGResponseInfo::getTook() {
    return took;
}
void
SWGResponseInfo::setTook(double took) {
    this->took = took;
}



} /* namespace Swagger */
