;; Auto-generated. Do not edit!


(when (boundp 'prueba_0::Arrow)
  (if (not (find-package "PRUEBA_0"))
    (make-package "PRUEBA_0"))
  (shadow 'Arrow (find-package "PRUEBA_0")))
(unless (find-package "PRUEBA_0::ARROW")
  (make-package "PRUEBA_0::ARROW"))

(in-package "ROS")
;;//! \htmlinclude Arrow.msg.html


(defclass prueba_0::Arrow
  :super ros::object
  :slots (_arrow ))

(defmethod prueba_0::Arrow
  (:init
   (&key
    ((:arrow __arrow) "")
    )
   (send-super :init)
   (setq _arrow (string __arrow))
   self)
  (:arrow
   (&optional __arrow)
   (if __arrow (setq _arrow __arrow)) _arrow)
  (:serialization-length
   ()
   (+
    ;; string _arrow
    4 (length _arrow)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _arrow
       (write-long (length _arrow) s) (princ _arrow s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _arrow
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _arrow (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get prueba_0::Arrow :md5sum-) "88a1badffe88bb4c1b4eb0ee47e6d7c1")
(setf (get prueba_0::Arrow :datatype-) "prueba_0/Arrow")
(setf (get prueba_0::Arrow :definition-)
      "string arrow

")



(provide :prueba_0/Arrow "88a1badffe88bb4c1b4eb0ee47e6d7c1")


