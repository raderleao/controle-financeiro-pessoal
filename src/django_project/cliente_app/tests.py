from django.test import TestCase

class TestClienteAPI(TestCase):
    def test_list_cliente(self):
        url = "/api/clientes/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        data = [
            {
                "id": "f73b2f8b-8f2f-41c4-b915-f0bb15ef7e40",
                "nome": "User1",
                "email": "user1@example.com",
                "is_active": True,
                "criado_por": "Bob",
                "atualizado_por": "Diana",
                "data_criacao": "2024-11-24T22:41:53.994638",
                "data_atualizacao": "2024-11-24T22:41:53.994647",
                "historico_alteracoes": [
                    {
                        "campo": "nome",
                        "valor_anterior": "OldUser1",
                        "valor_atual": "User1",
                        "data_alteracao": "2024-11-24T22:41:53.994650",
                        "alterado_por": "Eve"
                    },
                    {
                        "campo": "email",
                        "valor_anterior": "olduser1@example.com",
                        "valor_atual": "user1@example.com",
                        "data_alteracao": "2024-11-24T22:41:53.994657",
                        "alterado_por": "Charlie"
                    }
                ]
            },
            {
                "id": "4f8a7ce1-98ab-43a1-a8f5-7ed51ef5411f",
                "nome": "User2",
                "email": "user2@example.com",
                "is_active": True,
                "criado_por": "Alice",
                "atualizado_por": "Bob",
                "data_criacao": "2024-11-24T22:41:53.995085",
                "data_atualizacao": "2024-11-24T22:41:53.995096",
                "historico_alteracoes": [
                    {
                        "campo": "nome",
                        "valor_anterior": "OldUser2",
                        "valor_atual": "User2",
                        "data_alteracao": "2024-11-24T22:41:53.995100",
                        "alterado_por": "Bob"
                    },
                    {
                        "campo": "email",
                        "valor_anterior": "olduser2@example.com",
                        "valor_atual": "user2@example.com",
                        "data_alteracao": "2024-11-24T22:41:53.995128",
                        "alterado_por": "Bob"
                    }
                ]
            },
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)
