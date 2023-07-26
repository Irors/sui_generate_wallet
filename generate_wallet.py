import loguru
from pysui.abstracts import SignatureScheme
from pysui.sui.sui_crypto import recover_key_and_address
from pysui import SuiConfig


def generate_wallet(count):


    for i in range(count):
        cfg = SuiConfig.user_config(rpc_url="https://fullnode.mainnet.sui.io")
        _mnen, _address = cfg.create_new_keypair_and_address(SignatureScheme.ED25519)

        with open("wallet_sui.txt", "a") as file:
            file.write(f"{_mnen};{_address}\n")

    return loguru.logger.success("Кошельки успешно созданы")




if __name__ == "__main__":
    wallet_count = int(input("Введите число(количество создаваемых кошельков) : "))

    generate_wallet(wallet_count)
