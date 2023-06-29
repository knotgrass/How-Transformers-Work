import torch
from torch import nn, Tensor


class Attention(nn.Module):
    def __init__(self, word_size:int=512, embed_dim:int=64) -> None:
        super().__init__()
        self.embed_dim = embed_dim
        self.dim_K = torch.tensor(embed_dim)
        self.query = nn.Linear(in_features=word_size, out_features=embed_dim, bias=True)
        self.key  = nn.Linear(in_features=word_size, out_features=embed_dim, bias=True)
        self.value = nn.Linear(in_features=word_size, out_features=embed_dim, bias=True)


    def self_attention(self, Q:Tensor, K:Tensor, V:Tensor) -> Tensor:
        K_T = torch.transpose(K, 0, 1)
        score = torch.matmul(Q, K_T)  / torch.sqrt(self.dim_K)
        score = torch.softmax(score, dim=-1)
        Z = torch.matmul(score, V)
        return Z

    def forward(self, x:Tensor) -> Tensor:
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)
        Z = self.self_attention(Q, K, V)
        return Z


def test_forward_Attention():
    attention = Attention(word_size=512, embed_dim=64)

    # Tạo các embedding của 3 từ
    word1 = torch.randn(1, 512)  # Embedding của từ thứ nhất
    word2 = torch.randn(1, 512)  # Embedding của từ thứ hai
    word3 = torch.randn(1, 512)  # Embedding của từ thứ ba

    # Gộp các embedding thành một tensor đầu vào
    input_tensor = torch.cat([word1, word2, word3], dim=0)

    # Forward pass để tính toán đầu ra
    output = attention(input_tensor)

    # In ra kết quả đầu ra
    print(output)
    print(output.shape)
