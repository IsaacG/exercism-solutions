# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bank_account_pb2 as bank__account__pb2


class BankStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Open = channel.unary_unary(
                '/account.Bank/Open',
                request_serializer=bank__account__pb2.OpenRequest.SerializeToString,
                response_deserializer=bank__account__pb2.OpenResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/account.Bank/Close',
                request_serializer=bank__account__pb2.CloseRequest.SerializeToString,
                response_deserializer=bank__account__pb2.CloseResponse.FromString,
                )
        self.GetBalance = channel.unary_unary(
                '/account.Bank/GetBalance',
                request_serializer=bank__account__pb2.BalanceRequest.SerializeToString,
                response_deserializer=bank__account__pb2.BalanceResponse.FromString,
                )
        self.Deposit = channel.unary_unary(
                '/account.Bank/Deposit',
                request_serializer=bank__account__pb2.DepositRequest.SerializeToString,
                response_deserializer=bank__account__pb2.DepositResponse.FromString,
                )


class BankServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Open(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Open': grpc.unary_unary_rpc_method_handler(
                    servicer.Open,
                    request_deserializer=bank__account__pb2.OpenRequest.FromString,
                    response_serializer=bank__account__pb2.OpenResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=bank__account__pb2.CloseRequest.FromString,
                    response_serializer=bank__account__pb2.CloseResponse.SerializeToString,
            ),
            'GetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalance,
                    request_deserializer=bank__account__pb2.BalanceRequest.FromString,
                    response_serializer=bank__account__pb2.BalanceResponse.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=bank__account__pb2.DepositRequest.FromString,
                    response_serializer=bank__account__pb2.DepositResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.Bank', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bank(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Bank/Open',
            bank__account__pb2.OpenRequest.SerializeToString,
            bank__account__pb2.OpenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Bank/Close',
            bank__account__pb2.CloseRequest.SerializeToString,
            bank__account__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Bank/GetBalance',
            bank__account__pb2.BalanceRequest.SerializeToString,
            bank__account__pb2.BalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Bank/Deposit',
            bank__account__pb2.DepositRequest.SerializeToString,
            bank__account__pb2.DepositResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
