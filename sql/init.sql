SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: rsa; Type: TABLE; Schema: public; Owner: houdini_postgres
--

CREATE TABLE public.rsa (
    id integer NOT NULL,
    user_id integer,
    p numeric(500,0),
    q numeric(500,0),
    n numeric(500,0),
    phi numeric(500,0),
    e numeric(500,0),
    d numeric(500,0)
);


--ALTER TABLE public.rsa OWNER TO houdini_postgres;

--
-- Name: rsa_id_seq; Type: SEQUENCE; Schema: public; Owner: houdini_postgres
--

CREATE SEQUENCE public.rsa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.rsa_id_seq OWNER TO houdini_postgres;

--
-- Name: rsa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: houdini_postgres
--

ALTER SEQUENCE public.rsa_id_seq OWNED BY public.rsa.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: houdini_postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying,
    password character varying,
    w character varying,
    t timestamp without time zone
);


--ALTER TABLE public.users OWNER TO houdini_postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: houdini_postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.users_id_seq OWNER TO houdini_postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: houdini_postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: rsa id; Type: DEFAULT; Schema: public; Owner: houdini_postgres
--

ALTER TABLE ONLY public.rsa ALTER COLUMN id SET DEFAULT nextval('public.rsa_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: houdini_postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: rsa; Type: TABLE DATA; Schema: public; Owner: houdini_postgres
--

COPY public.rsa (id, user_id, p, q, n, phi, e, d) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: houdini_postgres
--

COPY public.users (id, login, password, w, t) FROM stdin;
\.


--
-- Name: rsa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: houdini_postgres
--

SELECT pg_catalog.setval('public.rsa_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: houdini_postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: rsa rsa_pkey; Type: CONSTRAINT; Schema: public; Owner: houdini_postgres
--

ALTER TABLE ONLY public.rsa
    ADD CONSTRAINT rsa_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: houdini_postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: rsa rsa_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: houdini_postgres
--

ALTER TABLE ONLY public.rsa
    ADD CONSTRAINT rsa_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

