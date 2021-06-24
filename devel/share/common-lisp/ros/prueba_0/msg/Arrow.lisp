; Auto-generated. Do not edit!


(cl:in-package prueba_0-msg)


;//! \htmlinclude Arrow.msg.html

(cl:defclass <Arrow> (roslisp-msg-protocol:ros-message)
  ((arrow
    :reader arrow
    :initarg :arrow
    :type cl:string
    :initform ""))
)

(cl:defclass Arrow (<Arrow>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Arrow>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Arrow)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name prueba_0-msg:<Arrow> is deprecated: use prueba_0-msg:Arrow instead.")))

(cl:ensure-generic-function 'arrow-val :lambda-list '(m))
(cl:defmethod arrow-val ((m <Arrow>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader prueba_0-msg:arrow-val is deprecated.  Use prueba_0-msg:arrow instead.")
  (arrow m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Arrow>) ostream)
  "Serializes a message object of type '<Arrow>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'arrow))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'arrow))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Arrow>) istream)
  "Deserializes a message object of type '<Arrow>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'arrow) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'arrow) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Arrow>)))
  "Returns string type for a message object of type '<Arrow>"
  "prueba_0/Arrow")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Arrow)))
  "Returns string type for a message object of type 'Arrow"
  "prueba_0/Arrow")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Arrow>)))
  "Returns md5sum for a message object of type '<Arrow>"
  "88a1badffe88bb4c1b4eb0ee47e6d7c1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Arrow)))
  "Returns md5sum for a message object of type 'Arrow"
  "88a1badffe88bb4c1b4eb0ee47e6d7c1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Arrow>)))
  "Returns full string definition for message of type '<Arrow>"
  (cl:format cl:nil "string arrow~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Arrow)))
  "Returns full string definition for message of type 'Arrow"
  (cl:format cl:nil "string arrow~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Arrow>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'arrow))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Arrow>))
  "Converts a ROS message object to a list"
  (cl:list 'Arrow
    (cl:cons ':arrow (arrow msg))
))
