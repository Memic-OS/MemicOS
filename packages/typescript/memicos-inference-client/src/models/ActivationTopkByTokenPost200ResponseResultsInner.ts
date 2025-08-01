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
import type { ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInner } from './ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInner';
import {
    ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerFromJSON,
    ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerFromJSONTyped,
    ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerToJSON,
    ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerToJSONTyped,
} from './ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInner';

/**
 * One token's TopK result, including its top features.
 * @export
 * @interface ActivationTopkByTokenPost200ResponseResultsInner
 */
export interface ActivationTopkByTokenPost200ResponseResultsInner {
    /**
     * The index of the token in the prompt.
     * @type {number}
     * @memberof ActivationTopkByTokenPost200ResponseResultsInner
     */
    tokenPosition: number;
    /**
     * The token string
     * @type {string}
     * @memberof ActivationTopkByTokenPost200ResponseResultsInner
     */
    token: string;
    /**
     * 
     * @type {Array<ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInner>}
     * @memberof ActivationTopkByTokenPost200ResponseResultsInner
     */
    topFeatures: Array<ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInner>;
}

/**
 * Check if a given object implements the ActivationTopkByTokenPost200ResponseResultsInner interface.
 */
export function instanceOfActivationTopkByTokenPost200ResponseResultsInner(value: object): value is ActivationTopkByTokenPost200ResponseResultsInner {
    if (!('tokenPosition' in value) || value['tokenPosition'] === undefined) return false;
    if (!('token' in value) || value['token'] === undefined) return false;
    if (!('topFeatures' in value) || value['topFeatures'] === undefined) return false;
    return true;
}

export function ActivationTopkByTokenPost200ResponseResultsInnerFromJSON(json: any): ActivationTopkByTokenPost200ResponseResultsInner {
    return ActivationTopkByTokenPost200ResponseResultsInnerFromJSONTyped(json, false);
}

export function ActivationTopkByTokenPost200ResponseResultsInnerFromJSONTyped(json: any, ignoreDiscriminator: boolean): ActivationTopkByTokenPost200ResponseResultsInner {
    if (json == null) {
        return json;
    }
    return {
        
        'tokenPosition': json['token_position'],
        'token': json['token'],
        'topFeatures': ((json['top_features'] as Array<any>).map(ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerFromJSON)),
    };
}

export function ActivationTopkByTokenPost200ResponseResultsInnerToJSON(json: any): ActivationTopkByTokenPost200ResponseResultsInner {
    return ActivationTopkByTokenPost200ResponseResultsInnerToJSONTyped(json, false);
}

export function ActivationTopkByTokenPost200ResponseResultsInnerToJSONTyped(value?: ActivationTopkByTokenPost200ResponseResultsInner | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'token_position': value['tokenPosition'],
        'token': value['token'],
        'top_features': ((value['topFeatures'] as Array<any>).map(ActivationTopkByTokenPost200ResponseResultsInnerTopFeaturesInnerToJSON)),
    };
}

