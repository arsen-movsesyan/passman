--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: account_attribute; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE account_attribute (
    id integer NOT NULL,
    acct_id integer NOT NULL,
    attr_id integer NOT NULL,
    acct_value character varying NOT NULL
);


--
-- Name: account_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE account_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: account_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE account_attribute_id_seq OWNED BY account_attribute.id;


--
-- Name: acct; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE acct (
    id integer NOT NULL,
    category_id integer NOT NULL,
    active boolean DEFAULT true NOT NULL,
    created_at date DEFAULT (now())::date NOT NULL,
    acct_name character varying NOT NULL,
    login character varying NOT NULL,
    passwd character varying NOT NULL,
    url character varying(2000) NOT NULL,
    description text
);


--
-- Name: attribute; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE attribute (
    id integer NOT NULL,
    attribute_name character varying NOT NULL
);


--
-- Name: acct_attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE acct_attribute_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: acct_attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE acct_attribute_id_seq OWNED BY attribute.id;


--
-- Name: address_history; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE address_history (
    id integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    str_address character varying NOT NULL,
    zip_code character(5) NOT NULL,
    comments text,
    city character varying NOT NULL,
    state character(2) NOT NULL
);


--
-- Name: address_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE address_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: address_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE address_history_id_seq OWNED BY address_history.id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE category (
    id integer NOT NULL,
    category_name character varying NOT NULL,
    description text
);


--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE category_id_seq OWNED BY category.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: new_acct_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE new_acct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: new_acct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE new_acct_id_seq OWNED BY acct.id;


--
-- Name: payment; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE payment (
    acct_id integer NOT NULL,
    due_date_day integer,
    month_frequency integer,
    auto_payment boolean DEFAULT false NOT NULL
);


--
-- Name: payment_history; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE payment_history (
    id integer NOT NULL,
    acct_id integer NOT NULL,
    payment_date date NOT NULL,
    payment_amount money NOT NULL,
    confirmation_code character varying
);


--
-- Name: payment_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE payment_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: payment_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE payment_history_id_seq OWNED BY payment_history.id;


--
-- Name: ssn; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE ssn (
    id integer NOT NULL,
    f_name character varying NOT NULL,
    l_name character varying NOT NULL,
    dob date NOT NULL,
    ssn_13 character(3),
    ssn_45 character(2),
    ssn_69 character(4)
);


--
-- Name: vehicle; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE vehicle (
    id integer NOT NULL,
    v_make character varying NOT NULL,
    v_model character varying NOT NULL,
    v_year character(4) NOT NULL,
    vin character varying NOT NULL,
    license_plate character varying NOT NULL,
    purchase_date date DEFAULT (now())::date NOT NULL,
    nonoperational_date date,
    retired date
);


--
-- Name: vehicle_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vehicle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vehicle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vehicle_id_seq OWNED BY vehicle.id;


--
-- Name: vehicle_registration; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE vehicle_registration (
    id integer NOT NULL,
    vehicle_id integer NOT NULL,
    registration_issue_date date NOT NULL,
    registration_expiration date NOT NULL
);


--
-- Name: vehicle_registration_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE vehicle_registration_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: vehicle_registration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE vehicle_registration_id_seq OWNED BY vehicle_registration.id;


--
-- Name: vehicle_registration_view; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW vehicle_registration_view AS
 SELECT v.id,
    v.v_make,
    v.v_model,
    v.v_year,
    v.license_plate,
    v.vin,
    vr.registration_issue_date AS last_issue_date,
    vr.registration_expiration AS expiration_date,
    (vr.registration_expiration - (now())::date) AS time_left
   FROM ((vehicle v
     JOIN vehicle_registration vr ON ((v.id = vr.vehicle_id)))
     JOIN ( SELECT vehicle_registration.vehicle_id,
            max(vehicle_registration.registration_issue_date) AS max_issue_date
           FROM vehicle_registration
          GROUP BY vehicle_registration.vehicle_id) __reg_max ON (((vr.vehicle_id = __reg_max.vehicle_id) AND (vr.registration_issue_date = __reg_max.max_issue_date))));


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY account_attribute ALTER COLUMN id SET DEFAULT nextval('account_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY acct ALTER COLUMN id SET DEFAULT nextval('new_acct_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY address_history ALTER COLUMN id SET DEFAULT nextval('address_history_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY attribute ALTER COLUMN id SET DEFAULT nextval('acct_attribute_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY category ALTER COLUMN id SET DEFAULT nextval('category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY payment_history ALTER COLUMN id SET DEFAULT nextval('payment_history_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vehicle ALTER COLUMN id SET DEFAULT nextval('vehicle_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY vehicle_registration ALTER COLUMN id SET DEFAULT nextval('vehicle_registration_id_seq'::regclass);


--
-- Name: account_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY account_attribute
    ADD CONSTRAINT account_attribute_pkey PRIMARY KEY (id);


--
-- Name: acct_acct_name_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY acct
    ADD CONSTRAINT acct_acct_name_key UNIQUE (acct_name);


--
-- Name: acct_attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY attribute
    ADD CONSTRAINT acct_attribute_pkey PRIMARY KEY (id);


--
-- Name: acct_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY acct
    ADD CONSTRAINT acct_pkey PRIMARY KEY (id);


--
-- Name: address_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY address_history
    ADD CONSTRAINT address_history_pkey PRIMARY KEY (id);


--
-- Name: category_category_name_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_category_name_key UNIQUE (category_name);


--
-- Name: category_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: payment_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY payment_history
    ADD CONSTRAINT payment_history_pkey PRIMARY KEY (id);


--
-- Name: payment_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (acct_id);


--
-- Name: ssn_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY ssn
    ADD CONSTRAINT ssn_pkey PRIMARY KEY (id);


--
-- Name: vehicle_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_pkey PRIMARY KEY (id);


--
-- Name: vehicle_registration_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY vehicle_registration
    ADD CONSTRAINT vehicle_registration_pkey PRIMARY KEY (id);


--
-- Name: attribute_attribute_name_idx; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE UNIQUE INDEX attribute_attribute_name_idx ON attribute USING btree (attribute_name);


--
-- Name: account_attribute_acct_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY account_attribute
    ADD CONSTRAINT account_attribute_acct_id_fkey FOREIGN KEY (acct_id) REFERENCES acct(id);


--
-- Name: account_attribute_attr_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY account_attribute
    ADD CONSTRAINT account_attribute_attr_id_fkey FOREIGN KEY (attr_id) REFERENCES attribute(id);


--
-- Name: acct_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acct
    ADD CONSTRAINT acct_category_id_fkey FOREIGN KEY (category_id) REFERENCES category(id);


--
-- Name: payment_acct_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY payment
    ADD CONSTRAINT payment_acct_id_fkey FOREIGN KEY (acct_id) REFERENCES acct(id);


--
-- Name: payment_history_acct_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY payment_history
    ADD CONSTRAINT payment_history_acct_id_fkey FOREIGN KEY (acct_id) REFERENCES payment(acct_id);


--
-- Name: vehicle_registration_vehicle_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY vehicle_registration
    ADD CONSTRAINT vehicle_registration_vehicle_id_fkey FOREIGN KEY (vehicle_id) REFERENCES vehicle(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

