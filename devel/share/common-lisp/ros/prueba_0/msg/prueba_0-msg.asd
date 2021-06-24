
(cl:in-package :asdf)

(defsystem "prueba_0-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Arrow" :depends-on ("_package_Arrow"))
    (:file "_package_Arrow" :depends-on ("_package"))
  ))