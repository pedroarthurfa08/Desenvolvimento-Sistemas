import Fastify, { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';
import { randomUUID } from 'crypto';

interface Book {
    id: string;
    title: string;
    description: string;
    category: string;
    pageCount: number;
    createdAt: Date;
}

let books: Book[] = [];

interface BookParams {
    bookId: string;
}

interface CreateBookBody {
    title: string;
    description: string;
    category: string;
    pageCount: number;
}

interface UpdateBookBody {
    title?: string;
    description?: string;
    category?: string;
    pageCount?: number;
}

const server: FastifyInstance = Fastify({
    logger: true,
});

server.get('/health', async (request: FastifyRequest, reply: FastifyReply) => {
    return { message: "It's working!" };
});

server.get('/books', async (request: FastifyRequest, reply: FastifyReply) => {
    return books;
});

server.get<{ Params: BookParams }>(
    '/books/:bookId',
    async (request: FastifyRequest<{ Params: BookParams }>, reply: FastifyReply) => {
        const bookId = request.params.bookId;
        const book = books.find((b) => b.id === bookId);
        if (!book) {
            reply.code(404).send({ message: 'Book not found' });
            return;
        }
        return book;
    }
);

server.post<{ Body: CreateBookBody }>(
    '/books',
    async (request: FastifyRequest<{ Body: CreateBookBody }>, reply: FastifyReply) => {
        const { title, description, category, pageCount } = request.body;
        if (!title || !description || !category || !pageCount) {
            reply.code(400).send({ message: 'Missing required fields: title, description, category, pageCount' });
            return;
        }
        const newBook: Book = {
            id: randomUUID(),
            title,
            description,
            category,
            pageCount,
            createdAt: new Date(),
        };
        books.push(newBook);
        reply.code(201);
        return newBook;
    }
);

server.put<{ Params: BookParams; Body: UpdateBookBody }>(
    '/books/:bookId',
    async (
        request: FastifyRequest<{ Params: BookParams; Body: UpdateBookBody }>,
        reply: FastifyReply
    ) => {
        const bookId = request.params.bookId;
        const { title, description, category, pageCount } = request.body;
        const bookIndex = books.findIndex((b) => b.id === bookId);
        if (bookIndex === -1) {
            reply.code(404).send({ message: 'Book not found' });
            return;
        }
        const updatedBook: Book = {
            ...books[bookIndex],
            title: title !== undefined ? title : books[bookIndex].title,
            description: description !== undefined ? description : books[bookIndex].description,
            category: category !== undefined ? category : books[bookIndex].category,
            pageCount: pageCount !== undefined ? pageCount : books[bookIndex].pageCount,
        };
        books[bookIndex] = updatedBook;
        return updatedBook;
    }
);

server.delete<{ Params: BookParams }>(
    '/books/:bookId',
    async (request: FastifyRequest<{ Params: BookParams }>, reply: FastifyReply) => {
        const bookId = request.params.bookId;
        const initialLength = books.length;
        books = books.filter((book) => book.id !== bookId);
        if (books.length === initialLength) {
            reply.code(404).send({ message: 'Book not found' });
            return;
        }
        reply.code(204).send();
    }
);

const start = async () => {
    try {
        await server.listen({ port: 3000 });
        console.log('Server listening on port 3000');
    } catch (err) {
        server.log.error(err);
        process.exit(1);
    }
};

start();