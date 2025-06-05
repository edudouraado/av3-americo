const express = require('express');
const { createClient } = require('@supabase/supabase-js'); // ✅ Importação corrigida
const morgan = require('morgan');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

const corsOptions = {
    origin: '*',
    credentials: true,
    optionSuccessStatus: 200,
};

app.use(cors(corsOptions));
app.use(morgan('combined'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// ✅ Criação do cliente Supabase com a forma correta
const supabase = createClient(
    'https://qhdfvqnpoocrwwfnycux.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFoZGZ2cW5wb29jcnd3Zm55Y3V4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc3ODY5NzEsImV4cCI6MjA2MzM2Mjk3MX0.8ANAxufG2dYnD8_By-SHDsz5qiRw6AsefGZVC_7RS_8'
);

// Rotas
app.get('/products', async (req, res) => {
    const { data, error } = await supabase.from('products').select();
    if (error) return res.status(500).send(error);
    console.log(`lists all products: ${JSON.stringify(data)}`);
    res.send(data);
});

app.get('/products/:id', async (req, res) => {
    console.log("id = " + req.params.id);
    const { data, error } = await supabase
        .from('products')
        .select()
        .eq('id', req.params.id);
    if (error) return res.status(500).send(error);
    console.log("retorno: " + JSON.stringify(data));
    res.send(data);
});

app.post('/products', async (req, res) => {
    const { error } = await supabase.from('products').insert({
        name: req.body.name,
        description: req.body.description,
        price: req.body.price,
    });
    if (error) return res.status(500).send(error);
    console.log("Produto criado:", req.body);
    res.send("created!!");
});

app.put('/products/:id', async (req, res) => {
    const { error } = await supabase
        .from('products')
        .update({
            name: req.body.name,
            description: req.body.description,
            price: req.body.price,
        })
        .eq('id', req.params.id);
    if (error) return res.status(500).send(error);
    res.send("updated!!");
});

app.delete('/products/:id', async (req, res) => {
    console.log("delete: " + req.params.id);
    const { error } = await supabase
        .from('products')
        .delete()
        .eq('id', req.params.id);
    if (error) return res.status(500).send(error);
    console.log("Produto deletado: " + req.params.id);
    res.send("deleted!!");
});

app.get('/', (req, res) => {
    res.send("Hello I am working my friend Supabase <3");
});

app.get('*', (req, res) => {
    res.send("Hello again I am working my friend to the moon and behind <3");
});

app.listen(3000, '0.0.0.0', () => {
    console.log(`> Ready on http://0.0.0.0:3000`);
});
