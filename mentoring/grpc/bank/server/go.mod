module example.com/bank/server

go 1.19

replace example.com/bank/proto => ../proto/

require (
	example.com/bank/account v0.0.0-00010101000000-000000000000
	example.com/bank/proto v0.0.0-00010101000000-000000000000
	google.golang.org/grpc v1.56.3
)

require (
	github.com/golang/protobuf v1.5.3 // indirect
	golang.org/x/net v0.33.0 // indirect
	golang.org/x/sys v0.28.0 // indirect
	golang.org/x/text v0.21.0 // indirect
	google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1 // indirect
	google.golang.org/protobuf v1.33.0 // indirect
)

replace example.com/bank/account => ../account/
