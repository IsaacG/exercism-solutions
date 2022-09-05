package main

import (
	"context"
	"errors"
	"example.com/bank/account"
	"flag"
	"fmt"
	"google.golang.org/grpc"
	"log"
	"net"

	pb "example.com/bank/proto"
)

type accountServer struct {
	pb.UnimplementedBankServer
	account *account.Account
}

var port = flag.Int("port", 50051, "The server port")

func (s *accountServer) Open(ctx context.Context, req *pb.OpenRequest) (*pb.OpenResponse, error) {
	log.Printf("Open request: %v", req)
	a := account.Open(req.Amount)
	if a == nil {
		return nil, errors.New("failed to open an account")
	}
	s.account = a
	return &pb.OpenResponse{}, nil
}

func (s *accountServer) Close(ctx context.Context, req *pb.CloseRequest) (*pb.CloseResponse, error) {
	log.Printf("Close request: %v", req)
	payout, ok := s.account.Close()
	if !ok {
		return nil, errors.New("failed to close the account")
	}
	s.account = nil
	return &pb.CloseResponse{Amount: payout}, nil
}

func (s *accountServer) GetBalance(ctx context.Context, req *pb.BalanceRequest) (*pb.BalanceResponse, error) {
	log.Printf("GetBalance request: %v", req)
	balance, ok := s.account.Balance()
	if !ok {
		return nil, errors.New("failed to get the account balance")
	}
	return &pb.BalanceResponse{Amount: balance}, nil
}

func (s *accountServer) Deposit(ctx context.Context, req *pb.DepositRequest) (*pb.DepositResponse, error) {
	log.Printf("Deposit request: %v", req)
	balance, ok := s.account.Deposit(req.Amount)
	if !ok {
		return nil, errors.New("failed to deposit")
	}
	return &pb.DepositResponse{Amount: balance}, nil
}

func newAccountServer() *accountServer {
	return &accountServer{account: nil}
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	var opts []grpc.ServerOption
	grpcServer := grpc.NewServer(opts...)
	pb.RegisterBankServer(grpcServer, newAccountServer())
	log.Printf("Starting server on port %d", *port)
	grpcServer.Serve(lis)
}
