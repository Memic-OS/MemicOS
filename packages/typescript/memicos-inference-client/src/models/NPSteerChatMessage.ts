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
/**
 * 
 * @export
 * @interface NPSteerChatMessage
 */
export interface NPSteerChatMessage {
    /**
     * The chat message
     * @type {string}
     * @memberof NPSteerChatMessage
     */
    content: string;
    /**
     * The role of the message (eg "model", "user", etc)
     * @type {string}
     * @memberof NPSteerChatMessage
     */
    role: string;
}

/**
 * Check if a given object implements the NPSteerChatMessage interface.
 */
export function instanceOfNPSteerChatMessage(value: object): value is NPSteerChatMessage {
    if (!('content' in value) || value['content'] === undefined) return false;
    if (!('role' in value) || value['role'] === undefined) return false;
    return true;
}

export function NPSteerChatMessageFromJSON(json: any): NPSteerChatMessage {
    return NPSteerChatMessageFromJSONTyped(json, false);
}

export function NPSteerChatMessageFromJSONTyped(json: any, ignoreDiscriminator: boolean): NPSteerChatMessage {
    if (json == null) {
        return json;
    }
    return {
        
        'content': json['content'],
        'role': json['role'],
    };
}

export function NPSteerChatMessageToJSON(json: any): NPSteerChatMessage {
    return NPSteerChatMessageToJSONTyped(json, false);
}

export function NPSteerChatMessageToJSONTyped(value?: NPSteerChatMessage | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        
        'content': value['content'],
        'role': value['role'],
    };
}

