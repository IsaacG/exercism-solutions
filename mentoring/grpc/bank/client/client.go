package main

import (
	"context"
	"example.com/bank/account"
	"flag"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"math/rand"
	"time"

	pb "example.com/bank/proto"
)

type accountServer struct {
	pb.UnimplementedBankServer
	account *account.Account
}

var serverAddr = flag.String("addr", "localhost:50051", "The server address in the format of host:port")

func Open(client pb.BankClient, initialDeposit int64) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	_, err := client.Open(ctx, &pb.OpenRequest{Amount: initialDeposit})
	if err != nil {
		log.Printf("client.Open failed: %v", err)
	} else {
		log.Println("Account opened")
	}
}

func Close(client pb.BankClient) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	resp, err := client.Close(ctx, &pb.CloseRequest{})
	if err != nil {
		log.Printf("client.Close failed: %v", err)
	} else {
		log.Printf("Account closed; payout = %d", resp.Amount)
	}
}

func Balance(client pb.BankClient, amount int64) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	resp, err := client.GetBalance(ctx, &pb.BalanceRequest{})
	if err != nil {
		log.Printf("client.GetBalance failed: %v", err)
	} else {
		log.Printf("Balance = %d", resp.Amount)
	}
}

func Deposit(client pb.BankClient, amount int64) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	resp, err := client.Deposit(ctx, &pb.DepositRequest{Amount: amount})
	if err != nil {
		log.Printf("client.Deposit failed: %v", err)
	} else {
		log.Printf("New balance = %d", resp.Amount)
	}
}

func main() {
	flag.Parse()
	var opts []grpc.DialOption
	opts = append(opts, grpc.WithTransportCredentials(insecure.NewCredentials()))

	conn, err := grpc.Dial(*serverAddr, opts...)
	if err != nil {
		log.Fatalf("fail to dial: %v", err)
	}
	defer conn.Close()
	rand.Seed(time.Now().UnixNano())
	client := pb.NewBankClient(conn)
	Open(client, 60)
	for i := 0; i < 10; i++ {
		amount := int64(rand.Intn(50))
		if amount%2 == 1 {
			amount = -amount
		}
		log.Printf("Deposit %d", amount)
		Deposit(client, amount)
	}
	Close(client)
}
