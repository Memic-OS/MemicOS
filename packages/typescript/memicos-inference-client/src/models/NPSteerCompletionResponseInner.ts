/* tslint:disable */
/* eslint-disable */
/**
 * MemicOS - Inference Server
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: johnny@memicos.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { NPSteerType } from './NPSteerType';
import {
    NPSteerTypeFromJSON,
    NPSteerTypeFromJSONTyped,
    NPSteerTypeToJSON,
    NPSteerTypeToJSONTyped,
} from './NPSteerType';

/**
 * A streamed steering/default response. Output is either the whole response or a chunk, depending on response type.
 * @export
 * @interface NPSteerCompletionResponseInner
 */
export interface NPSteerCompletionResponseInner {
    /**
     * 
     * @type {NPSteerType}
     * @memberof NPSteerCompletionResponseInner
     */
    type: NPSteerType;
    /**
     * 
     * @type {string}
     * @memberof NPSteerCompletionResponseInner
     */
    output: string;
}



/**
 * Check if a given object implements the NPSteerCompletionResponseInner interface.
 */
export function instanceOfNPSteerCompletionResponseInner(value: object): value is NPSteerCompletionResponseInner {
    if (!('type' in value) || value['type'] === undefined) return false;
    if (!('output' in value) || value['output'] === undefined) return false;
    return true;
}

export function NPSteerCompletionResponseInnerFromJSON(json: any): NPSteerCompletionResponseInner {
    return NPSteerCompletionResponseInnerFromJSONTyped(json, false);
}

export function NPSteerCompletionResponseInnerFromJSONTyped(json: any, ignoreDiscriminator: boolean): NPSteerCompletionResponseInner {
    if (json == null) {
        return json;
    }
    return {
        
        'type': NPSteerTypeFromJSON(json['type']),
        'output': json['output'],
    };
}

export function NPSteerCompletionResponseInnerToJSON(json: any): NPSteerCompletionResponseInner {
    return NPSteerCompletionResponseInnerToJSONTyped(json, false);
}

export function NPSteerCompletionResponseInnerToJSONTyped(value?: NPSteerCompletionResponseInner | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'type': NPSteerTypeToJSON(value['type']),
        'output': value['output'],
    };
}

