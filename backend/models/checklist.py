from database.banco_dados_checklist import conectar_banco_dados_checklist

class Checklist:
    def __init__(
        self,
        data,
        usuario,
        caminhao,
        tipo,
        pneu,
        estepe,
        adesivos_refletivos,
        cinto_seguranca,
        freio,
        tacografo,
        luzes,
        farois,
        indicadores,
        documentos_veiculo,
        observacao,
    ):
        
        self.data = data
        self.usuario = usuario
        self.caminhao = caminhao
        self.tipo = tipo
        self.pneu = pneu
        self.estepe = estepe
        self.adesivos_refletivos = adesivos_refletivos
        self.cinto_seguranca = cinto_seguranca
        self.freio = freio
        self.tacografo = tacografo
        self.luzes = luzes
        self.farois = farois
        self.indicadores = indicadores
        self.documentos_veiculo = documentos_veiculo
        self.observacao = observacao


    
    def inserir_checklist(self):

        conexao = conectar_banco_dados_checklist()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaChecklist (
        data,
        usuario,
        caminhao,
        tipo,
        pneu,
        estepe,
        adesivos_refletivos,
        cinto_seguranca,
        freio,
        tacografo,
        luzes,
        farois,
        indicadores,
        documentos_veiculo,
        observacao
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
                self.data,
                self.usuario,
                self.tipo,
                self.caminhao,
                self.pneu,
                self.estepe,
                self.adesivos_refletivos,
                self.cinto_seguranca,
                self.freio,
                self.tacografo,
                self.luzes,
                self.farois,
                self.indicadores,
                self.documentos_veiculo,
                self.observacao,
            )
        )

        conexao.commit()
        conexao.close()