// Auto-generated. Do not edit!

// (in-package prueba_0.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Arrow {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.arrow = null;
    }
    else {
      if (initObj.hasOwnProperty('arrow')) {
        this.arrow = initObj.arrow
      }
      else {
        this.arrow = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Arrow
    // Serialize message field [arrow]
    bufferOffset = _serializer.string(obj.arrow, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Arrow
    let len;
    let data = new Arrow(null);
    // Deserialize message field [arrow]
    data.arrow = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.arrow);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'prueba_0/Arrow';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '88a1badffe88bb4c1b4eb0ee47e6d7c1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string arrow
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Arrow(null);
    if (msg.arrow !== undefined) {
      resolved.arrow = msg.arrow;
    }
    else {
      resolved.arrow = ''
    }

    return resolved;
    }
};

module.exports = Arrow;
