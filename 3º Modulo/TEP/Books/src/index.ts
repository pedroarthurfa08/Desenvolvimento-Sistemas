import Fastify, {FastifyInstance, FastifyRequest, FastifyReply} from 'fastify';
import{ randomUUID } from 'crypto';
import { request } from 'http';

interface Book{
    id: string;
    title: string;
    descriptions:string;
    category: string;
    pageCount: number;
    creatAt: Date;
}

let books: Book[] = []

interface BookParams{
    bookId: string;
}

interface CreateBook {
    title: string;
    description: string;
    category: string;
    pageCount: number;
}

const server: FastifyInstance = Fastify({
    logger: true,
});

server.get('/health', async (request: FastifyRequest, reply: FastifyReply) => {
    return { message: "Está funcionando ;)"}
});

server.get('/books', async (request: FastifyRequest, reply: FastifyReply) => {
    return books;
});

server.get<{ Params: BookParams}>(
    '/books/:bookId',
    async (request: FastifyRequest<{ Params: BookParams}>, reply: FastifyReply) =>
{
    const bookId = request.params.bookId;
    const book = books.find((b) => b.id === bookId);

    if (!book){
        reply.code(404).send({message: 'Livro não encontrado :('});
        return;
    }
    return book;
}
);

server.post<{ Body: CreateBook }>('/books', async (
    request: FastifyRequest<{ Body: CreateBook }>,
    reply: FastifyReply)=> {
    const{title, description, category, pageCount} = request.body;
    if(!title || !description || !category || !pageCount) {
        reply.code(404).send({ messege: 'Campos obrigatórios ausentes: título, descrição, categoria, pageCount'});
        return;
    }

    const newBook: Book ={
        id: randomUUID(),
        title,
        description,
        category,
        pageCount,
        CreateAt: nem Date(),
    };
    books.push(newBook);

    reply.code(201);
    returnnemBook;
}
)