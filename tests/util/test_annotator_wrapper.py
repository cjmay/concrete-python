import mock
from mock import sentinel
import unittest

from concrete.services import Annotator
from concrete.util import annotator_wrapper


class AnnotatorClientWrapperTest(unittest.TestCase):
    def setUp(self):
        self.host = 'fake-host'
        self.port = 'fake-port'

        self.wrapper = annotator_wrapper.AnnotatorClientWrapper(self.host,
                                                                self.port)

    @mock.patch('concrete.services.Annotator.Client')
    @mock.patch.object(annotator_wrapper.ThriftFactory, 'createProtocol',
                       return_value=sentinel.protocol)
    @mock.patch.object(annotator_wrapper.ThriftFactory, 'createTransport')
    @mock.patch.object(annotator_wrapper.ThriftFactory, 'createSocket',
                       return_value=sentinel.socket)
    def test___enter__(self, mock_create_socket, mock_create_transport,
                       mock_create_protocol, mock_client):
        # create additional mocks for transport.open call...
        mock_transport = mock.Mock()
        mock_create_transport.return_value = mock_transport
        # ...and to verify the instantiation of the Annotator.Client
        mock_client.return_value = sentinel.client

        client = self.wrapper.__enter__()
        # check return value
        self.assertEquals(sentinel.client, client)

        # verify method invocations
        mock_create_socket.assert_called_once_with(self.host, self.port)
        mock_create_transport.assert_called_once_with(
            mock_create_socket.return_value)
        mock_create_protocol.assert_called_once_with(
            mock_create_transport.return_value)
        mock_client.assert_called_once_with(mock_create_protocol.return_value)

        mock_transport.open.assert_called_once_with()

    def test___exit__(self):
        # create mock for transport.close call
        mock_transport = mock.Mock()
        self.wrapper.transport = mock_transport

        self.wrapper.__exit__(mock.ANY, mock.ANY, mock.ANY)

        # verify invocations
        mock_transport.close.assert_called_once_with()
