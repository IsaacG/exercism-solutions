#!/bin/python

import grpc
import bank_account_pb2_grpc
import bank_account_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = bank_account_pb2_grpc.BankStub(channel)

while True:
    action = input("Action: ")
    if action == "open":
        print(stub.Open(bank_account_pb2.OpenRequest()))
    if action == "close":
        print(stub.Close(bank_account_pb2.CloseRequest()).amount)
    if action == "bal":
        print(stub.GetBalance(bank_account_pb2.BalanceRequest()).amount)
    if action.startswith("dep"):
        amt = int(action.split()[1])
        req = bank_account_pb2.DepositRequest()
        req.amount = amt
        print(stub.Deposit(req).amount)
