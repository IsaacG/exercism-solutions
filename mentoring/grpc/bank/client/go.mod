module example.com/bank/client

go 1.24.0

replace example.com/bank/account => ../account/

replace example.com/bank/proto => ../proto/

require (
	example.com/bank/account v0.0.0-00010101000000-000000000000
	example.com/bank/proto v0.0.0-00010101000000-000000000000
	google.golang.org/grpc v1.79.3
)

require (
	golang.org/x/net v0.48.0 // indirect
	golang.org/x/sys v0.39.0 // indirect
	golang.org/x/text v0.32.0 // indirect
	google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1 // indirect
	google.golang.org/protobuf v1.36.10 // indirect
)
