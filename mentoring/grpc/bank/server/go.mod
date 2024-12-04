module example.com/bank/server

go 1.19

replace example.com/bank/proto => ../proto/

require (
	example.com/bank/account v0.0.0-00010101000000-000000000000
	example.com/bank/proto v0.0.0-00010101000000-000000000000
	google.golang.org/grpc v1.53.0
)

require (
	github.com/golang/protobuf v1.5.2 // indirect
	golang.org/x/net v0.17.0 // indirect
	golang.org/x/sys v0.13.0 // indirect
	golang.org/x/text v0.13.0 // indirect
	google.golang.org/genproto v0.0.0-20230110181048-76db0878b65f // indirect
	google.golang.org/protobuf v1.28.1 // indirect
)

replace example.com/bank/account => ../account/
