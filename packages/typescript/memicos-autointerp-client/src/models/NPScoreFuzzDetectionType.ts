/* tslint:disable */
/* eslint-disable */
/**
 * MemicOS - AutoInterp Server
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: johnny@memicos.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * Type of scoring method, either fuzz or detection
 * @export
 */
export const NPScoreFuzzDetectionType = {
    Fuzz: 'FUZZ',
    Detection: 'DETECTION'
} as const;
export type NPScoreFuzzDetectionType = typeof NPScoreFuzzDetectionType[keyof typeof NPScoreFuzzDetectionType];


export function instanceOfNPScoreFuzzDetectionType(value: any): boolean {
    for (const key in NPScoreFuzzDetectionType) {
        if (Object.prototype.hasOwnProperty.call(NPScoreFuzzDetectionType, key)) {
            if (NPScoreFuzzDetectionType[key as keyof typeof NPScoreFuzzDetectionType] === value) {
                return true;
            }
        }
    }
    return false;
}

export function NPScoreFuzzDetectionTypeFromJSON(json: any): NPScoreFuzzDetectionType {
    return NPScoreFuzzDetectionTypeFromJSONTyped(json, false);
}

export function NPScoreFuzzDetectionTypeFromJSONTyped(json: any, ignoreDiscriminator: boolean): NPScoreFuzzDetectionType {
    return json as NPScoreFuzzDetectionType;
}

export function NPScoreFuzzDetectionTypeToJSON(value?: NPScoreFuzzDetectionType | null): any {
    return value as any;
}

export function NPScoreFuzzDetectionTypeToJSONTyped(value: any, ignoreDiscriminator: boolean): NPScoreFuzzDetectionType {
    return value as NPScoreFuzzDetectionType;
}

